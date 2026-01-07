# 어린이 한글 성경 (Kids Korean Bible)

저작권이 없는 World English Bible(WEB)을 기반으로 한 **어린이용 한글 성경** 프로젝트입니다.

## 프로젝트 정보

| 항목 | 내용 |
|------|------|
| **원본** | [World English Bible (WEB)](https://worldenglishbible.org) - Public Domain |
| **대상 연령** | 8-10세 (초등학교 저학년) |
| **범위** | 전체 성경 66권 (구약 39권 + 신약 27권) |
| **라이선스** | Public Domain (저작권 없음) |

## 번역 원칙

1. **쉬운 어휘**: 어린이가 이해할 수 있는 단어 사용
2. **짧은 문장**: 한 문장에 하나의 생각
3. **친근한 어조**: "~했어요", "~했습니다" 체
4. **하나님 존칭**: "하나님께서", "말씀하셨어요"

자세한 가이드라인은 [docs/translation-guide.md](docs/translation-guide.md)를 참조하세요.

## 프로젝트 구조

```
bible-korean-free/
├── README.md                 # 이 파일
├── source-web/               # WEB 성경 원본 (JSON)
│   └── json/
│       ├── genesis.json
│       └── ...
├── korean/                   # 번역된 한글 성경
│   ├── genesis.json
│   └── ...
├── scripts/                  # 도구 스크립트
│   ├── book_names.py         # 책 이름 매핑
│   └── parse_web.py          # JSON 파싱
└── docs/
    └── translation-guide.md  # 번역 가이드라인
```

## 번역 진행 상황

**전체 진행률: 59/66권 (89.4%)** - 2026년 1월 7일 기준

### 신약 (New Testament) - ✅ 완료 (27/27권)

| 책 | 한글 | 장 | 상태 |
|---|---|---|---|
| Matthew | 마태복음 | 28 | ✅ 완료 |
| Mark | 마가복음 | 16 | ✅ 완료 |
| Luke | 누가복음 | 24 | ✅ 완료 |
| John | 요한복음 | 21 | ✅ 완료 |
| Acts | 사도행전 | 28 | ✅ 완료 |
| Romans | 로마서 | 16 | ✅ 완료 |
| 1 Corinthians | 고린도전서 | 16 | ✅ 완료 |
| 2 Corinthians | 고린도후서 | 13 | ✅ 완료 |
| Galatians | 갈라디아서 | 6 | ✅ 완료 |
| Ephesians | 에베소서 | 6 | ✅ 완료 |
| Philippians | 빌립보서 | 4 | ✅ 완료 |
| Colossians | 골로새서 | 4 | ✅ 완료 |
| 1 Thessalonians | 데살로니가전서 | 5 | ✅ 완료 |
| 2 Thessalonians | 데살로니가후서 | 3 | ✅ 완료 |
| 1 Timothy | 디모데전서 | 6 | ✅ 완료 |
| 2 Timothy | 디모데후서 | 4 | ✅ 완료 |
| Titus | 디도서 | 3 | ✅ 완료 |
| Philemon | 빌레몬서 | 1 | ✅ 완료 |
| Hebrews | 히브리서 | 13 | ✅ 완료 |
| James | 야고보서 | 5 | ✅ 완료 |
| 1 Peter | 베드로전서 | 5 | ✅ 완료 |
| 2 Peter | 베드로후서 | 3 | ✅ 완료 |
| 1 John | 요한일서 | 5 | ✅ 완료 |
| 2 John | 요한이서 | 1 | ✅ 완료 |
| 3 John | 요한삼서 | 1 | ✅ 완료 |
| Jude | 유다서 | 1 | ✅ 완료 |
| Revelation | 요한계시록 | 22 | ✅ 완료 |

### 구약 (Old Testament) - 🟡 진행중 (32/39권)

#### 모세오경 (Pentateuch) - ✅ 완료 (5/5권)
| 책 | 한글 | 장 | 상태 |
|---|---|---|---|
| Genesis | 창세기 | 50 | ✅ 완료 |
| Exodus | 출애굽기 | 40 | ✅ 완료 |
| Leviticus | 레위기 | 27 | ✅ 완료 |
| Numbers | 민수기 | 36 | ✅ 완료 |
| Deuteronomy | 신명기 | 34 | ✅ 완료 |

#### 역사서 (Historical Books) - ✅ 완료 (12/12권)
| 책 | 한글 | 장 | 상태 |
|---|---|---|---|
| Joshua | 여호수아 | 24 | ✅ 완료 |
| Judges | 사사기 | 21 | ✅ 완료 |
| Ruth | 룻기 | 4 | ✅ 완료 |
| 1 Samuel | 사무엘상 | 31 | ✅ 완료 |
| 2 Samuel | 사무엘하 | 24 | ✅ 완료 |
| 1 Kings | 열왕기상 | 22 | ✅ 완료 |
| 2 Kings | 열왕기하 | 25 | ✅ 완료 |
| 1 Chronicles | 역대상 | 29 | ✅ 완료 |
| 2 Chronicles | 역대하 | 36 | ✅ 완료 |
| Ezra | 에스라 | 10 | ✅ 완료 |
| Nehemiah | 느헤미야 | 13 | ✅ 완료 |
| Esther | 에스더 | 10 | ✅ 완료 |

#### 시가서 (Poetry/Wisdom) - 🟡 진행중 (2/5권)
| 책 | 한글 | 장 | 상태 |
|---|---|---|---|
| Job | 욥기 | 42 | ⬜ 미시작 |
| Psalms | 시편 | 150 | ⬜ 미시작 |
| Proverbs | 잠언 | 31 | ⬜ 미시작 |
| Ecclesiastes | 전도서 | 12 | ✅ 완료 |
| Song of Solomon | 아가 | 8 | ✅ 완료 |

#### 대선지서 (Major Prophets) - 🟡 진행중 (1/5권)
| 책 | 한글 | 장 | 상태 |
|---|---|---|---|
| Isaiah | 이사야 | 66 | ⬜ 미시작 |
| Jeremiah | 예레미야 | 52 | ⬜ 미시작 |
| Lamentations | 애가 | 5 | ✅ 완료 |
| Ezekiel | 에스겔 | 48 | ⬜ 미시작 |
| Daniel | 다니엘 | 12 | ⬜ 미시작 |

#### 소선지서 (Minor Prophets) - ✅ 완료 (12/12권)
| 책 | 한글 | 장 | 상태 |
|---|---|---|---|
| Hosea | 호세아 | 14 | ✅ 완료 |
| Joel | 요엘 | 3 | ✅ 완료 |
| Amos | 아모스 | 9 | ✅ 완료 |
| Obadiah | 오바댜 | 1 | ✅ 완료 |
| Jonah | 요나 | 4 | ✅ 완료 |
| Micah | 미가 | 7 | ✅ 완료 |
| Nahum | 나훔 | 3 | ✅ 완료 |
| Habakkuk | 하박국 | 3 | ✅ 완료 |
| Zephaniah | 스바냐 | 3 | ✅ 완료 |
| Haggai | 학개 | 2 | ✅ 완료 |
| Zechariah | 스가랴 | 14 | ✅ 완료 |
| Malachi | 말라기 | 4 | ✅ 완료 |

**범례**: ✅ 완료 | 🟡 진행중 | ⬜ 미시작

## 샘플 번역 (창세기 1:1-5)

### 원문 (WEB)
> In the beginning, God created the heavens and the earth. The earth was formless and empty. Darkness was on the surface of the deep and God's Spirit was hovering over the surface of the waters. God said, "Let there be light," and there was light. God saw the light, and saw that it was good. God divided the light from the darkness. God called the light "day", and the darkness he called "night". There was evening and there was morning, the first day.

### 어린이 한글 번역
> 맨 처음에 하나님께서 하늘과 땅을 만드셨어요. 그때 땅에는 아무것도 없었고, 깜깜한 어둠만 가득했어요. 하나님의 영이 물 위를 움직이고 계셨어요. 하나님께서 "빛이 생겨라!" 하고 말씀하시자, 빛이 생겼어요. 하나님께서 빛을 보시고 참 좋다고 생각하셨어요. 그리고 빛과 어둠을 나누셨어요. 하나님께서 빛을 "낮"이라고 부르시고, 어둠을 "밤"이라고 부르셨어요. 저녁이 지나고 아침이 되니, 이것이 첫째 날이었어요.

## 사용 방법

### JSON 형식
```json
{
  "book": "Genesis",
  "bookKorean": "창세기",
  "chapters": [
    {
      "chapter": 1,
      "verses": [
        {
          "verse": 1,
          "original": "In the beginning...",
          "korean": "맨 처음에..."
        }
      ]
    }
  ]
}
```

## 기여하기

번역에 참여하고 싶으시면:

1. 이 저장소를 Fork 하세요
2. 번역할 책/장을 선택하세요
3. [번역 가이드라인](docs/translation-guide.md)을 따라 번역하세요
4. Pull Request를 보내주세요

## 라이선스

이 프로젝트는 **Public Domain**입니다. 자유롭게 사용, 수정, 배포할 수 있습니다.

원본 World English Bible은 저작권이 없는 공공 소유(Public Domain)이며, 이 한글 번역도 동일하게 공공 소유로 배포됩니다.

## 참고 자료

- [World English Bible](https://worldenglishbible.org)
- [WEB JSON Data (GitHub)](https://github.com/TehShrike/world-english-bible)
