#include <stdio.h>
struct pipe_info {
  int a, b, c;
};

int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  struct pipe_info pipes[m];
  int res[n+1];
  for (int i = 0; i < n + 1; i++){
    res[i] = -1;
  }
  for (int i = 0; i < m; i++){
    scanf("%d %d %d", &pipes[i].a, &pipes[i].b, &pipes[i].c);
  }
  int s, f;
  scanf("%d %d", &s, &f);
  res[s] = 0;

  for (int i = 1; i<n; i++)
    for (int j = 0; j < m; j++)
      if(res[pipes[j].a] != -1 && res[pipes[j].b] < res[pipes[j].a] + pipes[j].c)
        res[pipes[j].b] = res[pipes[j].a] + pipes[j].c;

  if (res[f] != -1)
    printf("%d", res[f]);
  else
    printf("%s","No solution");
  return 0;
}
