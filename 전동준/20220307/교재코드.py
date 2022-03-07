# 이하 교재에 있는 코드

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
# 해시 구성 노드
    def __init_(self,key : Any, value : Any, next : Node) -> None:
        # 초기화
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
# 해시 클래스 구현
    def __init__(self,capacity: int) -> None:
        # 초기화
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key : Any) -> int:
        # 해시값 구하기
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)

    def search(self, key : Any) -> Any:
        # 해시에서 키 값을 검색한 후 해당 값 반환
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:    # 해시에 어떤 값이 있을 때
            if p.key == key:    # 찾으려는 값과 키 값이 일치하면
                return p.value  # 검색 성공
            p = p.next          # 뒤쪽 노드 주목

    def add(self, key : Any, value : Any) -> bool:
        # 키가 key이고 값이 value인 원소 추가
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        # 해시 값 삭제 함수
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        # 모든 키 값 반환 함수
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end=' ')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end=' ')
                p = p.next
            print()