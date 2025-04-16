from docx import Document
from docx.shared import Pt
import os

def extract_styles_with_fonts(file_path):
    try:
        document = Document(file_path)
        styles = []
        for paragraph in document.paragraphs:
            font_name = None
            font_size = None
            if paragraph.runs:
                font_name = paragraph.runs[0].font.name
                font_size = paragraph.runs[0].font.size.pt if paragraph.runs[0].font.size else None
            styles.append({
                'text': paragraph.text,
                'style': paragraph.style.name,
                'font_name': font_name,
                'font_size': font_size
            })
        return styles
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "04:2025 HongZhong Hu_resume.docx")
    styles = extract_styles_with_fonts(file_path)
    if isinstance(styles, str):
        print(styles)
    else:
        for item in styles:
            print(f"Text: {item['text']}")
            print(f"Style: {item['style']}")
            print(f"Font Name: {item['font_name']}")
            print(f"Font Size: {item['font_size']} pt")
            print("---")