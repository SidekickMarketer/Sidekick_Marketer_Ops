"""
Strategy Document Parser

Parses uploaded strategy files (PDF, DOCX, TXT, Markdown) and extracts key information
using Claude to intelligently structure the content into strategy fields.
"""

import os
from anthropic import Anthropic
from typing import Optional

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def extract_text_from_file(file_content: bytes, filename: str) -> str:
    """Extract text content from various file types"""
    extension = filename.lower().split('.')[-1]

    if extension in ['txt', 'md', 'markdown']:
        return file_content.decode('utf-8', errors='ignore')

    elif extension == 'pdf':
        try:
            import io
            # Try PyMuPDF (fitz) first - it's more reliable
            try:
                import fitz  # PyMuPDF
                pdf_doc = fitz.open(stream=file_content, filetype="pdf")
                text = ""
                for page in pdf_doc:
                    text += page.get_text()
                pdf_doc.close()
                return text
            except ImportError:
                # Fall back to PyPDF2
                from PyPDF2 import PdfReader
                pdf_file = io.BytesIO(file_content)
                reader = PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                return text
        except Exception as e:
            return f"[Error extracting PDF: {str(e)}]"

    elif extension in ['docx', 'doc']:
        try:
            import io
            from docx import Document
            doc_file = io.BytesIO(file_content)
            doc = Document(doc_file)
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        except Exception as e:
            return f"[Error extracting DOCX: {str(e)}]"

    else:
        # Try to decode as text
        try:
            return file_content.decode('utf-8', errors='ignore')
        except:
            return "[Unsupported file type]"


def parse_strategy_document(file_content: bytes, filename: str, client_name: str) -> dict:
    """
    Parse a strategy document and extract structured strategy information.

    Returns a dict with extracted fields that can be used to populate the strategy form.
    """
    # Extract text from file
    text_content = extract_text_from_file(file_content, filename)

    if text_content.startswith("[Error") or text_content == "[Unsupported file type]":
        return {"error": text_content, "raw_content": ""}

    if not text_content.strip():
        return {"error": "No text content found in file", "raw_content": ""}

    # Truncate if too long (Claude context limit consideration)
    if len(text_content) > 50000:
        text_content = text_content[:50000] + "\n\n[Content truncated due to length...]"

    # Use Claude to intelligently extract strategy information
    prompt = f"""Analyze this strategy/brand document for "{client_name}" and extract relevant information.

DOCUMENT CONTENT:
{text_content}

Extract and return the following information in JSON format. Only include fields you can confidently extract from the document. Use null for any fields not found.

Return ONLY valid JSON with this exact structure:
{{
    "brand_voice": "Description of the brand's voice and tone (string or null)",
    "tone_keywords": ["keyword1", "keyword2"] or null,
    "content_pillars": ["pillar1", "pillar2"] or null,
    "target_audience": "Description of target audience (string or null)",
    "audience_pain_points": ["pain point 1", "pain point 2"] or null,
    "industry": "One of: saas, ecommerce, local_business, professional_services, health_wellness, real_estate, coaching_consulting, restaurant_hospitality, or default",
    "unique_selling_points": ["usp1", "usp2"] or null,
    "key_messages": ["message1", "message2"] or null,
    "topics_to_avoid": ["topic1", "topic2"] or null,
    "hashtags_primary": ["hashtag1", "hashtag2"] or null,
    "hashtags_secondary": ["hashtag1", "hashtag2"] or null,
    "platforms": ["instagram", "facebook", etc.] or null,
    "additional_notes": "Any other relevant strategy info not captured above (string or null)",
    "summary": "Brief 2-3 sentence summary of the overall strategy"
}}

Be thorough in your extraction. Look for:
- Brand voice/tone descriptions
- Target customer/audience descriptions
- Product/service descriptions that indicate USPs
- Content themes or pillars
- Any mentioned social platforms
- Hashtag recommendations
- Topics or language to avoid
- Key messages or taglines

Return ONLY the JSON, no other text."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = response.content[0].text.strip()

        # Clean up response if needed
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]

        import json
        extracted = json.loads(response_text.strip())
        extracted["raw_content"] = text_content[:5000]  # Store first 5k chars for reference
        return extracted

    except Exception as e:
        return {
            "error": f"Failed to parse document: {str(e)}",
            "raw_content": text_content[:5000]
        }


def merge_extracted_strategies(existing: dict, new_data: dict) -> dict:
    """
    Merge newly extracted strategy data with existing data.
    New non-null values override existing values.
    Arrays are merged/deduplicated.
    """
    result = existing.copy()

    for key, value in new_data.items():
        if value is None or key in ['error', 'raw_content', 'summary']:
            continue

        if key not in result or result[key] is None:
            result[key] = value
        elif isinstance(value, list) and isinstance(result.get(key), list):
            # Merge and deduplicate lists
            combined = result[key] + value
            result[key] = list(dict.fromkeys(combined))  # Preserve order, remove dupes
        elif isinstance(value, str) and value:
            # For strings, only override if existing is empty
            if not result.get(key):
                result[key] = value

    return result
