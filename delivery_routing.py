from collections import deque
from dataclasses import dataclass
from heapq import heappush, heappop
from math import hypot
from typing import List, Tuple, Dict, Optional


@dataclass
class SearchResult:
    path: List[str]
    distance_km: float
    nodes_expanded: int


class DeliveryNetwork:

    def __init__(self):
        self.coordinates: Dict[str, Tuple[float, float]] = {
            "Warehouse": (0, 0),
            "North Hub": (2, 4),
            "West Junction": (3, 1),
            "Central Hub": (5, 3),
            "Riverside": (6, 0),
            "East Junction": (8, 3),
            "Hillcrest": (9, 6),
            "South Depot": (4, -3),
            "Customer": (11, 1),
        }
        self.graph: Dict[str, Dict[str, float]] = {
            node: {} for node in self.coordinates
        }
        self._add_road("Warehouse", "North Hub", 5.0)
        self._add_road("Warehouse", "West Junction", 3.5)
        self._add_road("Warehouse", "South Depot", 5.0)
        self._add_road("North Hub", "West Junction", 4.0)
        self._add_road("North Hub", "Central Hub", 4.0)
        self._add_road("North Hub", "Hillcrest", 8.0)
        self._add_road("West Junction", "Central Hub", 3.0)
        self._add_road("West Junction", "South Depot", 4.0)
        self._add_road("Central Hub", "Riverside", 4.0)
        self._add_road("Central Hub", "East Junction", 3.5)
        self._add_road("Central Hub", "Hillcrest", 4.5)
        self._add_road("Riverside", "East Junction", 4.0)
        self._add_road("Riverside", "Customer", 6.0)
        self._add_road("East Junction", "Customer", 3.5)
        self._add_road("East Junction", "Hillcrest", 3.0)
        self._add_road("South Depot", "RiverSide", 7.0)


def _add_road(self, a: str, b: str, km: float) -> None:
    self.graph[a][b] = km
    self.graph[b][a] = km


def heuristic(self, node: str, goal: str) -> float:
    x1, y1 = self.coordinates[node]
    x2, y2 = self.coordinates[goal]
    return 0.5 * hypot(x2 - x1, y2 - y1)


def path_distance(self, path: List[str]) -> float:
    return sum(self.graph[a][b] for a, b in zip(path, path[1:]))


class BreadthFirstSearch:

    @staticmethod
    def search(
        network: DeliveryNetwork, start: str, goal: str
    ) -> Optional[SearchResult]:
        queue = deque([start])
        parent = {start: None}
        expanded = 0

        while queue:
            current = queue.popleft()
            expanded += 1
            if current == goal:
                break
            for neighbor in network.graph[current]:
                if neighbor not in parent:
                    parent[neighbor] = current
                    queue.append(neighbor)

        if goal not in parent:
            return None
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
        return SearchResult(path, network.path_distance(path), expanded)
