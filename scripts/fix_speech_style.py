#!/usr/bin/env python3
"""
어투 일관성 수정 스크립트
프로젝트 방향: 8-10세 어린이용, "~해요" 체 (친근한 존댓말)

수정 패턴:
1. "~것이다" → "~거예요"
2. "~이다." → "~이에요."
3. "~겠다." → "~겠어요."
4. "~했다." → "~했어요."
5. "~한다." → "~해요."
6. "~된다." → "~돼요."
"""

import glob
import re

def fix_speech_style():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        '것이다 → 거예요': 0,
        '이다." → 이에요."': 0,
        '겠다." → 겠어요."': 0,
        '했다." → 했어요."': 0,
        '한다." → 해요."': 0,
        '였다." → 였어요."': 0,
        '없다." → 없어요."': 0,
        '있다." → 있어요."': 0,
        '된다." → 돼요."': 0,
        '난다." → 나요."': 0,
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. "~것이다" → "~거예요" (가장 많은 패턴)
        # 다양한 패턴: 할 것이다, 될 것이다, 올 것이다, 줄 것이다 등
        count = len(re.findall(r'것이다', content))
        stats['것이다 → 거예요'] += count
        content = content.replace('것이다', '거예요')

        # 2. "~이다." → "~이에요." (문장 끝)
        count = len(re.findall(r'이다\."', content))
        stats['이다." → 이에요."'] += count
        content = content.replace('이다."', '이에요."')

        # 3. "~겠다." → "~겠어요."
        count = len(re.findall(r'겠다\."', content))
        stats['겠다." → 겠어요."'] += count
        content = content.replace('겠다."', '겠어요."')

        # 4. "~했다." → "~했어요."
        count = len(re.findall(r'했다\."', content))
        stats['했다." → 했어요."'] += count
        content = content.replace('했다."', '했어요."')

        # 5. "~한다." → "~해요."
        count = len(re.findall(r'한다\."', content))
        stats['한다." → 해요."'] += count
        content = content.replace('한다."', '해요."')

        # 6. "~였다." → "~였어요."
        count = len(re.findall(r'였다\."', content))
        stats['였다." → 였어요."'] += count
        content = content.replace('였다."', '였어요."')

        # 7. "~없다." → "~없어요."
        count = len(re.findall(r'없다\."', content))
        stats['없다." → 없어요."'] += count
        content = content.replace('없다."', '없어요."')

        # 8. "~있다." → "~있어요."
        count = len(re.findall(r'있다\."', content))
        stats['있다." → 있어요."'] += count
        content = content.replace('있다."', '있어요."')

        # 9. "~된다." → "~돼요."
        count = len(re.findall(r'된다\."', content))
        stats['된다." → 돼요."'] += count
        content = content.replace('된다."', '돼요."')

        # 10. "~난다." → "~나요."
        count = len(re.findall(r'난다\."', content))
        stats['난다." → 나요."'] += count
        content = content.replace('난다."', '나요."')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("어투 일관성 수정 시작...")
    print("목표: 8-10세 어린이용 '~해요' 체\n")

    stats, modified_files = fix_speech_style()

    print("수정 통계:")
    total = 0
    for pattern, count in stats.items():
        if count > 0:
            print(f"  {pattern}: {count}건")
            total += count
    print(f"  ─────────────────")
    print(f"  총계: {total}건")

    print(f"\n수정된 파일: {len(modified_files)}개")
    for f in sorted(modified_files):
        print(f"  - {f}")

    print("\n완료!")
