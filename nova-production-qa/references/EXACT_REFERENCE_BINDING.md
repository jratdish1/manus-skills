# Exact Reference Binding

Use this reference whenever a Nova package is reviewed, audited, approved, generated, or published. The Nova Bible, scene registry, script package, prompt, and production policy are part of the audit scope. Do not rely on mutable branch URLs or an unversioned local copy when asserting a compliant final result.

## Bind Every Required Source

For every governing input, record all five fields in the package evidence:

| Field | Requirement |
|---|---|
| Repository | Repository owner/name holding the source of truth. |
| Branch | Branch used only for navigation; do not treat it as immutable evidence. |
| Commit SHA | Exact commit that contained the reviewed source. |
| File path | Exact file path at that commit. |
| File SHA-256 | Checksum of the file content used in the review. |

Use commit-pinned URLs when supplying source material to an external reviewer:

```text
https://github.com/<owner>/<repo>/blob/<commit-sha>/<file-path>
```

## Minimum Nova Package Bindings

Record exact bindings for:

1. `nova-bible-audit/SKILL.md` from `jratdish1/manus-skills`.
2. `nova-production-qa/SKILL.md` from `jratdish1/manus-skills`.
3. `VETS_STANDING_AUDIT_DIRECTIVE.md` from `jratdish1/manus-skills`.
4. The canonical Nova character Bible in the private source-of-truth repository.
5. The Nova Scene Diversity Bible in the private source-of-truth repository.
6. The approved episode script, Grok image prompt, negative prompt, captions, and production notes.
7. The final video, final audio, final still(s), and representative QA frames.

## Staleness Rule

If any bound reference, source file, final asset, or checksum changes after audit evidence is created, do not use the former evidence to certify the altered package. Return:

```text
AUDIT STALE — HEAD CHANGED
```

Then rebuild the binding table and rerun the applicable audit.

## Source Unavailable Rule

If a required private reference cannot be accessed or its exact revision cannot be confirmed, do not infer its content. Return:

```text
SOURCE_UNAVAILABLE
```

Request the exact commit-pinned source, a verified archive, or an approved local hash record before proceeding.

## Example Evidence Entry

```text
source_reference_bindings:
  - role: Canonical Nova Character Bible
    repository: jratdish1/knowledge-base
    branch: main
    commit_sha: <40-character SHA>
    file_path: nova/<canonical-bible-file>.md
    file_sha256: <64-character SHA-256>
    reviewer_url: https://github.com/jratdish1/knowledge-base/blob/<commit-sha>/nova/<canonical-bible-file>.md
```

Do not include a private URL in public documentation or public evidence. Store private review links only in the authorized private evidence record.
