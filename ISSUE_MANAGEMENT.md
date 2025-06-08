# GitHub Issue Management Workflow

<!-- filepath: /Users/jdfalk/repos/github.com/jdfalk/gcommon/ISSUE_MANAGEMENT.md -->
<!-- file: ISSUE_MANAGEMENT.md -->

This repository uses automated GitHub Actions for issue management. **All development work must include proper issue status tracking**.

## 🤖 Automated Issue Updates

The `update-issues.yml` workflow processes an `issue_updates.json` file on every push to main branch.

### Supported Actions

| Action   | Purpose               | Required Fields | Optional Fields                                 |
| -------- | --------------------- | --------------- | ----------------------------------------------- |
| `create` | Create new issue      | `title`, `body` | `labels`, `assignees`, `milestone`              |
| `update` | Modify existing issue | `number`        | `title`, `body`, `state`, `labels`, `assignees` |
| `delete` | Remove issue          | `number`        | None                                            |

### File Format

```json
[
  {
    "action": "create",
    "title": "New Feature: Add metrics dashboard",
    "body": "Detailed description...",
    "labels": ["enhancement", "metrics"]
  },
  {
    "action": "update",
    "number": 42,
    "state": "closed",
    "labels": ["completed"]
  }
]
```

## 📋 Required Development Workflow

### 1. Starting Work on an Issue

```bash
# Assign yourself and mark in progress
echo '[{"action": "update", "number": ISSUE_NUMBER, "assignees": ["your-github-username"], "labels": ["in-progress"]}]' > issue_updates.json
git add issue_updates.json
git commit -m "Start work on issue #ISSUE_NUMBER: [Brief Description]"
git push
```

### 2. During Development

- **Reference Issues**: Include issue numbers in commit messages (`#ISSUE_NUMBER`)
- **Progress Updates**: Add comments to issues for significant progress
- **Label Changes**: Update labels if priority or scope changes

### 3. Completing Work

```bash
# Close issue and mark completed
echo '[{"action": "update", "number": ISSUE_NUMBER, "state": "closed", "labels": ["completed"]}]' > issue_updates.json
git add issue_updates.json
git commit -m "Complete issue #ISSUE_NUMBER: [What was accomplished]"
git push
```

## 🎯 Project-Specific Workflow

### For Protobuf Implementation

Each protobuf implementation issue requires:

1. **Start**: Assign issue, add "in-progress" label
2. **Implement**: Follow 1-1-1 pattern, test compilation
3. **Validate**: Run `make proto-compile` and `buf lint`
4. **Complete**: Close issue, add "completed" label
5. **Update Status**: Modify module completion percentage in README.md

### Example: Implementing Metrics Module

```bash
# Start work on metrics messages (Issue #68)
echo '[{"action": "update", "number": 68, "assignees": ["your-username"], "labels": ["in-progress", "module:metrics"]}]' > issue_updates.json
git add issue_updates.json && git commit -m "Start metrics messages implementation #68" && git push

# After implementing all 27 message files
echo '[{"action": "update", "number": 68, "state": "closed", "labels": ["completed", "module:metrics"]}]' > issue_updates.json
git add issue_updates.json && git commit -m "Complete #68: Implemented all 27 metrics message types" && git push
```

## 🔧 Common Use Cases

### Bulk Update Multiple Issues

```json
[
  {"action": "update", "number": 68, "assignees": ["dev1"], "labels": ["in-progress"]},
  {"action": "update", "number": 69, "assignees": ["dev2"], "labels": ["in-progress"]},
  {"action": "update", "number": 70, "assignees": ["dev3"], "labels": ["in-progress"]}
]
```

### Create Issue with Full Details

```json
[
  {
    "action": "create",
    "title": "Bug: Auth service memory leak",
    "body": "## Problem\nMemory usage increases over time...\n## Steps to Reproduce\n1. Start auth service\n2. ...",
    "labels": ["bug", "module:auth", "priority:high"],
    "assignees": ["maintainer"]
  }
]
```

### Mark Issue as Blocked

```json
[
  {
    "action": "update",
    "number": 75,
    "labels": ["blocked", "dependency:external"],
    "body": "Blocked waiting for upstream protobuf release..."
  }
]
```

## ⚠️ Important Notes

- **Always Clean Up**: Remove `issue_updates.json` after each push to avoid repeated actions
- **Test Actions**: Review JSON format carefully to avoid errors
- **Status Accuracy**: Keep issue states current for accurate project tracking
- **Workflow Compliance**: All work must follow this process for project visibility

## 🚀 Benefits

- **Automated Tracking**: No manual GitHub UI navigation required
- **Batch Operations**: Update multiple issues simultaneously
- **Version Control**: Issue state changes are tracked in git history
- **Consistency**: Standardized workflow across all contributors
- **Project Visibility**: Accurate real-time status for all work

---

**📍 Quick Reference**: Always include issue numbers in commit messages and update issue status when starting/completing work!
