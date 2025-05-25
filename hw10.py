import os
import pickle

filename = 'score.bin'

if os.path.exists(filename):
    with open(filename, 'rb') as f:
        scores = pickle.load(f)
else:
    scores = []
    while True:
        score = int(input(f'#{len(scores)+1}? '))
        if score < 0:
            break
        scores.append(score)
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

print('개인점수:', *scores)
print('평균:', sum(scores)/len(scores) if scores else 0)
