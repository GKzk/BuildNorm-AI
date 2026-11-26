"""Layout-aware text extraction from text-based PDF files.

This module preserves page numbers and text-block bounding boxes. It does not
perform OCR and does not claim to reconstruct tables or normative hierarchy.
"""

from dataclasses import dataclass
import pymupdf


class PdfExtractionError(ValueError):
    """Raised when a PDF cannot be opened or processed."""


@dataclass(frozen=True, slots=True)
class PdfTextBlock:
    """A text block and its bounding box in PDF page coordinates."""

    text: str
    x0: float
    y0: float
    x1: float
    y1: float


@dataclass(frozen=True, slots=True)
class PdfPage:
    """Extracted content for one 1-based PDF page."""

    page_number: int
    text: str
    blocks: tuple[PdfTextBlock, ...]


@dataclass(frozen=True, slots=True)
class PdfExtraction:
    """Text extraction result for a complete PDF document."""

    page_count: int
    pages: tuple[PdfPage, ...]


def extract_pdf_text(pdf_bytes: bytes) -> PdfExtraction:
    """Extract text and text-block geometry from PDF bytes.

    Scanned pages may return empty text. OCR is intentionally out of scope for
    this first implementation.
    """
    if not pdf_bytes:
        raise PdfExtractionError("The PDF file is empty.")

    try:
        document = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    except (fitz.FileDataError, RuntimeError) as exc:
        raise PdfExtractionError("The file is not a readable PDF.") from exc

    with document:
        if document.needs_pass:
            raise PdfExtractionError("Password-protected PDFs are not supported.")

        if document.page_count == 0:
            raise PdfExtractionError("The PDF contains no pages.")

        extracted_pages: list[PdfPage] = []
        for page_index, page in enumerate(document):
            raw_blocks: list[PdfTextBlock] = []
            for block in page.get_text("blocks", sort=True):
                if len(block) < 7 or block[6] != 0:
                    continue

                text = str(block[4]).strip()
                if not text:
                    continue

                raw_blocks.append(
                    PdfTextBlock(
                        text=text,
                        x0=float(block[0]),
                        y0=float(block[1]),
                        x1=float(block[2]),
                        y1=float(block[3]),
                    )
                )

            extracted_pages.append(
                PdfPage(
                    page_number=page_index + 1,
                    text=page.get_text("text", sort=True).strip(),
                    blocks=tuple(raw_blocks),
                )
            )

        return PdfExtraction(
            page_count=document.page_count,
            pages=tuple(extracted_pages),
        )
