<!-- file: .github/github-projects-configuration.md -->
<!-- version: 1.0.0 -->
<!-- guid: 9f3e7b2a-4d8c-4f1a-9e6b-7c2a5d8f3e9b -->

# GitHub Projects Configuration Guide

This document outlines the recommended GitHub Projects configuration with automatic sorting based on our repository labels.

## Current Status

GitHub Projects (the new Projects beta/v2) can be configured programmatically via the GraphQL API, but it requires complex setup and organization-level permissions. Currently, manual configuration is the most practical approach.

## Recommended Projects Structure

Based on our 137 repository labels, here are the recommended GitHub Projects with their associated labels:

### 1. 🚀 Feature Development Project

**Purpose**: Track new feature development and enhancements

**Auto-sort Rules (Labels)**:

- `type:feature` - New feature development
- `type:enhancement` - Improvement to existing feature
- `feature` - New feature development
- `enhancement` - New feature or request
- `size:epic` - Epic change (multiple days/weeks)
- `size:large` - Large change (1-2 days)

**Columns**:

- Backlog (status:todo)
- Ready (status:ready)
- In Progress (status:in-progress)
- Review (status:needs-review, status:review)
- Done (closed issues)

### 2. 🐛 Bug Fixes & Maintenance Project

**Purpose**: Track bug fixes and maintenance work

**Auto-sort Rules (Labels)**:

- `type:bug` - Something isn't working
- `bug` - Something isn't working
- `bugfix` - Bug fix work
- `type:maintenance` - Maintenance and housekeeping
- `type:security` - Security related issues
- `security` - Security related issues
- `critical` - Critical priority - immediate attention required
- `priority:critical` - Critical priority - immediate attention required

**Columns**:

- Critical Issues (priority:critical, critical)
- Ready to Fix (status:ready)
- In Progress (status:in-progress)
- Testing (status:review)
- Resolved (closed issues)

### 3. 📚 Documentation & Standards Project

**Purpose**: Track documentation updates and coding standards

**Auto-sort Rules (Labels)**:

- `type:documentation` - Improvements or additions to documentation
- `documentation` - Improvements or additions to documentation
- `type:refactor` - Code refactoring without feature changes
- `refactor` - Code refactoring work
- `gcommon-refactor` - gcommon refactoring work
- `project:gcommon-refactor` - gcommon refactor initiative

**Columns**:

- Documentation Needed
- In Progress
- Review
- Published

### 4. 🔧 Infrastructure & DevOps Project

**Purpose**: Track CI/CD, automation, and infrastructure work

**Auto-sort Rules (Labels)**:

- `workflow:ci-cd` - Continuous integration and deployment
- `ci-cd` - Continuous integration and deployment
- `workflow:github-actions` - GitHub Actions workflows
- `github-actions` - GitHub Actions related work
- `workflow:automation` - Automation and tooling
- `automation` - Automation scripts and tools
- `workflow:deployment` - Deployment and release management
- `dependencies` - Dependencies management
- `external-dependency` - Depends on external systems or libraries

**Columns**:

- Infrastructure Backlog
- In Development
- Testing
- Deployed

### 5. 🎯 Module-Specific Projects

#### Auth Module Project

**Auto-sort Rules (Labels)**:

- `module:auth` - Authentication and authorization
- `auth` - Authentication and authorization

#### Protobuf Implementation Project

**Auto-sort Rules (Labels)**:

- `project:protobuf-implementation` - Protocol buffer implementation work
- `module:proto` - Protocol buffer related
- `proto` - Protocol buffer work
- `type:protobuf` - Protocol buffer work
- `tech:protobuf` - Protocol buffer definitions
- `protobuf` - Protocol buffer definitions

#### Media Processing Project

**Auto-sort Rules (Labels)**:

- `project:media` - Media processing and handling
- `project:subtitles` - Subtitle processing and conversion
- `project:transcription` - Audio transcription features
- `project:whisper` - Whisper ASR integration
- `media` - Media processing and handling
- `transcription` - Audio transcription features
- `whisper` - Whisper ASR integration

### 6. 🏷️ Technology-Specific Projects

#### Go Development Project

**Auto-sort Rules (Labels)**:

- `tech:go` - Go programming language
- `go` - Go programming language

#### Python Development Project

**Auto-sort Rules (Labels)**:

- `tech:python` - Python programming language
- `python` - Python programming language

#### JavaScript/TypeScript Project

**Auto-sort Rules (Labels)**:

- `tech:javascript` - JavaScript programming language
- `javascript` - JavaScript programming language
- `tech:typescript` - TypeScript programming language

## Implementation Steps

### Manual Configuration (Recommended)

1. **Create Projects**: Go to the repository's Projects tab and create the projects listed above
2. **Set up Views**: Create different views (Board, Table, Timeline) for each project
3. **Configure Automation**: Use GitHub's built-in automation rules to move items based on labels
4. **Add Filters**: Set up saved filters for each label category

### Automation Rules to Set Up

For each project, configure these automation rules:

```
When: Item is added to project
If: Label contains [specific labels for this project]
Then: Move to [appropriate column]

When: Issue is closed
Then: Move to "Done" column

When: Label "status:in-progress" is added
Then: Move to "In Progress" column

When: Label "status:needs-review" is added
Then: Move to "Review" column
```

## Priority-Based Sorting

Within each project, use these priority labels for sorting:

- `priority:critical` / `critical` - Top priority
- `priority:high` / `high` - High priority
- `priority:medium` / `medium` - Medium priority
- `priority:low` / `low` - Low priority

## Size-Based Planning

Use size labels for sprint planning:

- `size:epic` - Epic change (multiple days/weeks)
- `size:large` - Large change (1-2 days)
- `size:medium` - Medium change (half day)
- `size:small` - Small change (1-2 hours)

## Status Workflow

Standard workflow using status labels:

1. `status:todo` - To do - not started
2. `status:ready` - Ready for implementation
3. `status:in-progress` - Work in progress
4. `status:needs-review` - Needs code review
5. `status:review` - Task is ready for review
6. `status:blocked` - Blocked by external dependencies
7. Closed - Completed

## Maintenance

- Review and update project configurations monthly
- Add new labels to appropriate projects as they are created
- Archive completed projects and create new ones as needed
- Monitor automation rules and adjust as workflow evolves

## Notes

- GitHub Projects v2 automation is powerful but requires careful setup
- Consider using GitHub's Project templates for consistency
- Regularly review and clean up old or unused labels
- Some automation may require GitHub Pro or organization features

This configuration provides comprehensive project management while leveraging our extensive label system for automatic organization.
