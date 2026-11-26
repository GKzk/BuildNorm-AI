import fitz
import pytest

from app.documents.pdf_extractor import PdfExtractionError, extract_pdf_text


def make_test_pdf() -> bytes:
    document = fitz.open()
    first_page = document.new_page()
    first_page.insert_text((72, 72), "СП TEST — раздел 1")
    second_page = document.new_page()
    second_page.insert_text((72, 72), "Пункт 2.1. Требование для теста.")
    pdf_bytes = document.tobytes()
    document.close()
    return pdf_bytes


def test_extracts_text_with_one_based_page_numbers_and_blocks() -> None:
    result = extract_pdf_text(make_test_pdf())

    assert result.page_count == 2
    assert [page.page_number for page in result.pages] == [1, 2]
    assert "СП TEST — раздел 1" in result.pages[0].text
    assert "Пункт 2.1." in result.pages[1].text
    assert result.pages[0].blocks
    assert result.pages[0].blocks[0].x0 >= 0
    assert result.pages[0].blocks[0].x1 > result.pages[0].blocks[0].x0


def test_rejects_empty_input() -> None:
    with pytest.raises(PdfExtractionError, match="empty"):
        extract_pdf_text(b"")


def test_rejects_non_pdf_input() -> None:
    with pytest.raises(PdfExtractionError, match="readable PDF"):
        extract_pdf_text(b"this is not a PDF")
