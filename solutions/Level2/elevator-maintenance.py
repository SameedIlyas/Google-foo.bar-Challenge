def solution(l):
    def versions(l):
        numbers = l.split('.')
        return tuple(int(num) for num in numbers)

    sorted_versions = sorted(l, key=versions)
    return sorted_versions
