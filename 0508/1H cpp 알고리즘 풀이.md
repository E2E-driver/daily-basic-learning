- **[프로그래머스] 택배상자 꺼내기 : https://school.programmers.co.kr/learn/courses/30/lessons/389478**

  

  - **1. 올림 계산 (Ceiling Calculation)**
    $$
      \text{rows} = \left\lceil \frac{n}{w} \right\rceil              = \frac{n + w - 1}{w}
    $$
    

    - 정수형 나눗셈(integer division)만으로 올림값(ceiling)을 구하는 표준 기법입니다.
    - `(n + w - 1)/w` 수식이 왜 올림(ceiling) 결과를 주나요?
      - A1. 정수 `n` 을 `w` 로 나눌 때 나머지(remainder) 가 있을 경우 `+w-1` 로 올려 담아 한 단계 높은 몫(quotient)을 얻게 합니다.

  

  - **2. `break` 문은 가장 가까운(innermost) 반복문(loop) 또는 `switch` 문을 빠져나가게 합니다.**

    지금 코드에서 `break;` 는 `for` 문 안이 아니라 `if` 블록 내부에 위치해 있으므로, 가장 가까운 반복문은 `while` 이고, 따라서 `while` 문 전체를 즉시 종료합니다.

    ```cpp
    while (floor != rows) {
        if (floor % 2 != 0) {
            if (number > n)
                break;      // ← 이 지점에서 가장 가까운 반복문인 while을 탈출!
            for (int i = 0; i < cols; i++) {
                space[floor][i] = number++;
            }
        }
        …
    }
    ```

    - `break` 는 if 문을 빠져나오게 하지 않고, while 반복문을 바로 종료합니다.
    - 만약 `for` 문 안에서 `break` 를 쓰면 `for` 만 빠져나가고, 그 외부의 `while` 은 계속 실행됩니다**.**

  

  - **3. `continue` 는 가장 가까운 반복문의 현재 반복(iteration) 만 건너뛰고, 다음 반복으로 넘어갑니다.**

  

  - **4. ++ 전위 연산자(prefix)와 후위 연산자(postfix)** 

    4.1 단순 루프

    ```cpp
    cpp복사편집for (int i = 0; i < 10; ++i) {   // 권장: prefix
        // ...
    }
    ```

    4.2 표현식(Expression) 내 차이

    ```cpp
    cpp복사편집int i = 5;
    
    // 1) prefix
    int x = ++i * 2;  // i→6, x→12
    
    // 2) postfix
    i = 5;
    int y = i++ * 2;  // y→10 (i가 5일 때 곱셈), 이후 i→6
    ```

    4.3 사용자 정의 타입

    ```cpp
    cpp복사편집struct BigInt {
        BigInt& operator++() { /* 전위 */ return *this; }
        BigInt operator++(int) {  // 후위: int dummy 인자로 구분
            BigInt tmp(*this);
            ++(*this);
            return tmp;  // 복사본 반환
        }
    };
    ```

    