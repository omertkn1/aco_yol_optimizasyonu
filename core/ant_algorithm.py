
import numpy as np

class AntColonyOptimization:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        self.distances = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.n_ants, self.n_best, self.n_iterations = n_ants, n_best, n_iterations
        self.decay, self.alpha, self.beta = decay, alpha, beta
        self.best_path, self.best_dist, self.history = None, float('inf'), []

    def run(self):
        for _ in range(self.n_iterations):
            paths = []
            for _ in range(self.n_ants):
                path = self._gen_path(0)
                dist = self._dist(path)
                paths.append((path, dist))

            self._update(paths)
            self.history.append(self.best_dist)
        return self.best_path, self.best_dist, self.history

    def _gen_path(self, start):
        path, visited = [start], {start}
        for _ in range(len(self.distances) - 1):
            move = self._pick(self.pheromone[path[-1]], self.distances[path[-1]], visited)
            path.append(move)
            visited.add(move)
        path.append(start)
        return path

    def _pick(self, pher, dist, visited):
        with np.errstate(divide='ignore', invalid='ignore'):
            row = (pher ** self.alpha) * ((1.0 / (dist + 1e-6)) ** self.beta)
        row[list(visited)] = 0
        if row.sum() == 0:
            return np.random.choice(list(set(range(len(self.distances))) - visited))
        return np.random.choice(range(len(self.distances)), p=row/row.sum())

    def _dist(self, path):
        return sum(self.distances[path[i]][path[i+1]] for i in range(len(path)-1))

    def _update(self, paths):
        sorted_p = sorted(paths, key=lambda x: x[1])
        if sorted_p[0][1] < self.best_dist:
            self.best_dist, self.best_path = sorted_p[0][1], sorted_p[0][0]

        self.pheromone *= self.decay
        for p, d in sorted_p[:self.n_best]:
            for i in range(len(p)-1):
                self.pheromone[p[i]][p[i+1]] += 1.0 / (d + 1e-6)

