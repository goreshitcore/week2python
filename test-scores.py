test_scores = [78, 92.5, 84, 88.2, 90, 76, 85.6]
print("Test Scores:", test_scores)

avg_test_score = sum(test_scores) / len(test_scores)
print("Average Score: {:.2f}".format(avg_test_score))

highest_score = max(test_scores)
lowest_score = min(test_scores)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)

sorted_scores_desc = sorted(test_scores, reverse=True)
print("Sorted Scores (Descending):", sorted_scores_desc)
