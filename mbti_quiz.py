# 이 프로그램은 Gemini를 이용해 만들었습니다.
# 20251126_ver.01

import collections

def run_mbti_quiz():
    """
    12문항으로 구성된 간단한 MBTI 검사를 실행하고 결과를 출력합니다.
    """
    
    # 4가지 MBTI 차원에 대한 카운트를 저장할 딕셔너리
    # E/I, S/N, T/F, J/P 순서로 카운트
    # 'E', 'S', 'T', 'J'가 선택되면 +1, 'I', 'N', 'F', 'P'가 선택되면 -1
    scores = collections.defaultdict(int)

    # 12개의 질문 문항 (3문항씩 4가지 차원에 할당)
    # 각 질문은 [질문 텍스트, E/I, S/N, T/F, J/P 중 어떤 차원인지]를 포함
    questions = [
        # E/I (외향/내향) - 1, 5, 9
        ["1. 주말에 친구들과 에너지를 얻는 편이다. (예: E, 아니오: I)", 'EI'],
        ["5. 혼자 조용히 생각할 시간을 가질 때 더 편안함을 느낀다. (예: I, 아니오: E)", 'IE'],
        ["9. 새로운 사람들을 만나는 것에 거부감이 없다. (예: E, 아니오: I)", 'EI'],
        
        # S/N (감각/직관) - 2, 6, 10
        ["2. 구체적이고 현실적인 사실에 집중하는 편이다. (예: S, 아니오: N)", 'SN'],
        ["6. 큰 그림과 미래의 가능성을 상상하는 것을 좋아한다. (예: N, 아니오: S)", 'NS'],
        ["10. 일을 할 때 순서나 과정을 중요하게 생각한다. (예: S, 아니오: N)", 'SN'],

        # T/F (사고/감정) - 3, 7, 11
        ["3. 결정을 내릴 때 논리와 객관적인 분석을 중요하게 여긴다. (예: T, 아니오: F)", 'TF'],
        ["7. 타인의 감정을 공감하고 배려하는 것이 가장 중요하다고 생각한다. (예: F, 아니오: T)", 'FT'],
        ["11. 비판을 할 때 솔직하고 단호하게 표현하는 편이다. (예: T, 아니오: F)", 'TF'],

        # J/P (판단/인식) - 4, 8, 12
        ["4. 계획을 세우고 그 계획을 따르는 것을 선호한다. (예: J, 아니오: P)", 'JP'],
        ["8. 상황에 따라 유연하게 대처하며 즉흥적인 활동을 즐긴다. (예: P, 아니오: J)", 'PJ'],
        ["12. 일이 미완성으로 남아있어도 크게 불편함을 느끼지 않는다. (예: P, 아니오: J)", 'PJ'],
    ]

    print("--- 📝 간단 MBTI 검사 시작 (총 12문항) ---")
    
    # 질문에 대한 답변 받기
    for i, (question, dimension) in enumerate(questions):
        # dimension[0] = 첫 번째 유형 (예: E, S, T, J)
        # dimension[1] = 두 번째 유형 (예: I, N, F, P)

        while True:
            # 사용자에게 '예'/'아니오'로 답변 요청 (입력 오류 방지)
            answer = input(f"{question} [예/아니오]: ").strip().lower()

            if answer == '예':
                # '예'는 일반적으로 첫 번째 유형(E, S, T, J)에 해당
                if dimension == 'EI' or dimension == 'SN' or dimension == 'TF' or dimension == 'JP':
                    scores[dimension] += 1
                    result_char = dimension[0]
                # '예'가 두 번째 유형(I, N, F, P)에 해당 (질문이 반대로 구성된 경우)
                elif dimension == 'IE' or dimension == 'NS' or dimension == 'FT' or dimension == 'PJ':
                    scores[dimension[::-1]] -= 1 # 반대 유형 점수 차감
                    result_char = dimension[1]
                break

            elif answer == '아니오':
                # '아니오'는 일반적으로 두 번째 유형(I, N, F, P)에 해당
                if dimension == 'EI' or dimension == 'SN' or dimension == 'TF' or dimension == 'JP':
                    scores[dimension] -= 1
                    result_char = dimension[1]
                # '아니오'가 첫 번째 유형(E, S, T, J)에 해당 (질문이 반대로 구성된 경우)
                elif dimension == 'IE' or dimension == 'NS' or dimension == 'FT' or dimension == 'PJ':
                    scores[dimension[::-1]] += 1 # 반대 유형 점수 추가
                    result_char = dimension[0]
                break
            
            else:
                print("⚠️ '예' 또는 '아니오'로만 답해주세요.")

    # 최종 MBTI 유형 계산 및 결과 출력
    mbti_type = ""
    
    # 1. E/I (외향/내향)
    # E/I 차원 점수의 합이 0보다 크면 E, 0보다 작거나 같으면 I
    ei_score = scores.get('EI', 0) + scores.get('IE', 0) * (-1 if 'IE' == 'EI'[::-1] else 1)
    mbti_type += 'E' if scores['EI'] >= 0 else 'I'

    # 2. S/N (감각/직관)
    # S/N 차원 점수의 합이 0보다 크면 S, 0보다 작거나 같으면 N
    mbti_type += 'S' if scores['SN'] >= 0 else 'N'

    # 3. T/F (사고/감정)
    # T/F 차원 점수의 합이 0보다 크면 T, 0보다 작거나 같으면 F
    mbti_type += 'T' if scores['TF'] >= 0 else 'F'
    
    # 4. J/P (판단/인식)
    # J/P 차원 점수의 합이 0보다 크면 J, 0보다 작거나 같으면 P
    mbti_type += 'J' if scores['JP'] >= 0 else 'P'


    print("\n--- ✅ 검사 결과 ---")
    print(f"**당신의 MBTI 유형은: {mbti_type}**")
    
    # 해설 제공
    print("\n--- 💡 유형 해설 ---")
    provide_mbti_interpretation(mbti_type)
    print("----------------------")


def provide_mbti_interpretation(mbti_type):
    """
    간단한 MBTI 유형 해설을 제공합니다.
    """
    
    interpretations = {
        # 분석가형 (NT)
        "INTJ": "용의주도한 전략가, 뛰어난 분석력과 비전을 가진 독립적인 사색가입니다.",
        "INTP": "논리적인 사색가, 지적인 호기심이 많고 문제 해결 능력이 탁월합니다.",
        "ENTJ": "대담한 통솔자, 강력한 리더십과 추진력으로 목표를 달성하는 CEO 유형입니다.",
        "ENTP": "뜨거운 논쟁을 즐기는 변론가, 창의적이며 새로운 아이디어를 탐구하는 것을 좋아합니다.",
        
        # 외교관형 (NF)
        "INFJ": "선도하는 활동가, 깊은 통찰력과 강한 신념으로 이상적인 세상을 추구합니다.",
        "INFP": "열정적인 중재자, 온화하고 이타적이며 자신의 가치에 충실합니다.",
        "ENFJ": "정의로운 사회 운동가, 사람들에게 영감을 주고 긍정적인 변화를 이끌어냅니다.",
        "ENFP": "재기발랄한 활동가, 창의적이고 사교적이며 삶을 즐기는 낙천가입니다.",
        
        # 관리자형 (SJ)
        "ISTJ": "청렴결백한 논리주의자, 사실에 근거하여 책임감 있게 일을 처리합니다.",
        ""
        "ISFJ": "용감한 수호자, 헌신적이며 타인을 돕는 것에 보람을 느낍니다.",
        "ESTJ": "엄격한 관리자, 체계적이며 현실적인 목표를 효율적으로 추진합니다.",
        "ESFJ": "사교적인 외교관, 친절하고 협조적이며 주변 사람들과 조화롭게 지냅니다.",
        
        # 탐험가형 (SP)
        "ISTP": "만능 재주꾼, 도구를 다루는 능력이 뛰어나며 논리적인 해결사입니다.",
        "ISFP": "호기심 많은 예술가, 따뜻하고 겸손하며 미적 감각이 뛰어납니다.",
        "ESTP": "모험을 즐기는 사업가, 현실적이고 활동적이며 위험을 감수하는 것을 두려워하지 않습니다.",
        "ESFP": "자유로운 영혼의 연예인, 낙천적이며 사람들과의 상호작용을 즐깁니다.",
    }

    print(f"**{mbti_type}**: {interpretations.get(mbti_type, '죄송합니다. 이 유형에 대한 간략한 해설을 찾을 수 없습니다.')}")
    print("\n*주의: 이 프로그램은 12문항으로 간략하게 제작되었으므로, 실제 MBTI 검사와는 차이가 있을 수 있습니다.")


# 프로그램 실행
run_mbti_quiz()