# Paper comparison

| configuration | paper_accuracy | reproduced_accuracy | accuracy_absolute_difference | accuracy_percentage_point_difference | paper_macro_f1 | reproduced_macro_f1 | macro_f1_absolute_difference | parity_status | structural_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tfidf_logistic_regression | 0.921000 | 0.804970 | 0.116030 | -11.603041 | 0.918000 | 0.803974 | 0.114026 | RED |  |
| tfidf_svm | 0.932000 | 0.807558 | 0.124442 | -12.444209 | 0.928000 | 0.806758 | 0.121242 | RED |  |
| tfidf_random_forest | 0.919000 | 0.823217 | 0.095783 | -9.578271 | 0.914000 | 0.824086 | 0.089914 | RED |  |
| tfidf_knn | 0.854000 | 0.730038 | 0.123962 | -12.396247 | 0.855000 | 0.739226 | 0.115774 | RED |  |
| structural_documented_18_logistic_regression | 0.781000 | 0.738579 | 0.042421 | -4.242099 | 0.763000 | 0.728839 | 0.034161 | RED | Only 18 documented structural features were implemented. |
| structural_documented_18_svm | 0.791000 | 0.766015 | 0.024985 | -2.498473 | 0.774000 | 0.762058 | 0.011942 | RED | Only 18 documented structural features were implemented. |
| structural_documented_18_random_forest | 0.778000 | 0.738708 | 0.039292 | -3.929157 | 0.752000 | 0.727939 | 0.024061 | RED | Only 18 documented structural features were implemented. |
| structural_documented_18_knn | 0.783000 | 0.733402 | 0.049598 | -4.959764 | 0.762000 | 0.728999 | 0.033001 | RED | Only 18 documented structural features were implemented. |

Structural rows use `structural_documented_18`, not an unspecified 23-feature implementation. Matching macro-F1 does not prove semantic label reproduction.
