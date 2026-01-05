"""
WEB 성경 JSON 파싱 및 절 추출
"""
import json
from pathlib import Path
from typing import Iterator
from dataclasses import dataclass

from book_names import get_korean_name, BOOK_ORDER


@dataclass
class Verse:
    """성경 한 절을 나타내는 클래스"""
    book: str
    book_korean: str
    chapter: int
    verse: int
    text: str

    def to_dict(self) -> dict:
        return {
            "book": self.book,
            "bookKorean": self.book_korean,
            "chapter": self.chapter,
            "verse": self.verse,
            "original": self.text,
            "korean": ""  # 번역 후 채워짐
        }


def parse_book(json_path: Path) -> Iterator[Verse]:
    """JSON 파일에서 절을 추출"""
    book_name = json_path.stem  # 파일 이름에서 확장자 제거
    book_korean = get_korean_name(book_name)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        if item.get("type") == "paragraph text":
            yield Verse(
                book=book_name,
                book_korean=book_korean,
                chapter=item["chapterNumber"],
                verse=item["verseNumber"],
                text=item["value"].strip()
            )


def extract_chapter(json_path: Path, chapter: int) -> list[Verse]:
    """특정 장만 추출"""
    verses = []
    for verse in parse_book(json_path):
        if verse.chapter == chapter:
            verses.append(verse)
    return verses


def get_all_books(source_dir: Path) -> list[Path]:
    """모든 성경 책 파일을 순서대로 반환"""
    json_files = list(source_dir.glob("*.json"))

    # BOOK_ORDER 순서대로 정렬
    def sort_key(path: Path) -> int:
        name = path.stem.lower()
        try:
            return BOOK_ORDER.index(name)
        except ValueError:
            return 999  # 목록에 없으면 맨 뒤로

    return sorted(json_files, key=sort_key)


def count_verses(json_path: Path) -> dict:
    """책의 장별 절 수 계산"""
    chapters = {}
    for verse in parse_book(json_path):
        if verse.chapter not in chapters:
            chapters[verse.chapter] = 0
        chapters[verse.chapter] = max(chapters[verse.chapter], verse.verse)
    return chapters


if __name__ == "__main__":
    # 테스트
    source_dir = Path(__file__).parent.parent / "source-web" / "json"

    print("=== 성경 책 목록 ===")
    for book_path in get_all_books(source_dir):
        korean_name = get_korean_name(book_path.stem)
        verse_counts = count_verses(book_path)
        total_chapters = len(verse_counts)
        total_verses = sum(verse_counts.values())
        print(f"{korean_name} ({book_path.stem}): {total_chapters}장, {total_verses}절")

    print("\n=== 창세기 1장 미리보기 ===")
    genesis = source_dir / "genesis.json"
    for verse in extract_chapter(genesis, 1)[:5]:
        print(f"{verse.chapter}:{verse.verse} {verse.text[:50]}...")
