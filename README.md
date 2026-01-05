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

### 구약 (Old Testament)

| 책 | 한글 | 상태 |
|---|---|---|
| Genesis | 창세기 | 🟡 1장 완료 |
| Exodus | 출애굽기 | ⬜ 미시작 |
| ... | ... | ... |

### 신약 (New Testament)

| 책 | 한글 | 상태 |
|---|---|---|
| Matthew | 마태복음 | ⬜ 미시작 |
| Mark | 마가복음 | ⬜ 미시작 |
| ... | ... | ... |

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
  "book": "genesis",
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
