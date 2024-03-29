# 이상한 술집

https://www.acmicpc.net/problem/13702

## 풀이

이분 탐색을 활용하여 풀이할 수 있습니다.\
우선 이 문제에서 최대로 많이 막걸리를 분배할 수 있는 값을 구할 수 있습니다.
- `sum(capacitys) // people_c` 모든 용량을 합한 값을 인원수에 나눈 값

이제 이 값을 최대값(right)로 0을 left로 지정합니다. 이 후에 아래 로직으로 이분 탐색을 합니다.\
- 1명당 막걸리 용량을 얼마나 줄 지 구합니다 `(right+left) // 2` = `mid`
  - mid가 0이면 1로 할당
- mid의 값으로 주전자들에서 몇명을 분배해줄 수 있는지 개수를 구합니다.
  - 개수가 인원수보다 적을 경우 right에 mid-1 값을 할당
  - 개수가 인원수보다 크거나 같을 경우 left에 mid+1 값을 할당
- 위를 반복하다 left가 right보다 커질 경우 그만한다.

이 때 right의 값이 주전자들로 사람들에게 최대한 많은 용량으로 분배할 수 있는 값입니다.
