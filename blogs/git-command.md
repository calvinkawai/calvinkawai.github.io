---
tags:
  - sde-tools
links:
  - "[[020 CS]]"
title: Git Commands
created: 2024-08-24
---

# Add specific part of the file

> When you work on a feature that requires a lot changes, but maybe you have some small part ready for review and only want to commit specific part of the file

```
git add -p {file_name}
```

# Cherry pick

> Work on another branch but need changes from current branches, note that you can add commit-ref list to pick multiple commits in once

```
git cherry-pick {commit-ref}
```
