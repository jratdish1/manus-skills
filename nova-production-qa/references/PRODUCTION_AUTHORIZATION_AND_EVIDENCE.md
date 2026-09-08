# Production Authorization and Evidence Workflow

Use this workflow before changing a live posting state, scheduling a post, modifying a production configuration, or claiming an `AUDIT STATUS: PASS — GRADE A` result for a Nova package.

## Purpose

Create an explicit, attributable, exact-artifact approval record that binds VETS authorization, final assets, source references, audit evidence, and rollback information. This workflow does not publish content by itself.

## Required Record

Create one non-secret approval record per attempted production action at:

```text
<private-source-of-truth-repo>/nova/audit-evidence/<YYYY-MM-DD>/<package-id>/approval-record.md
```

Use a stable package ID such as `NOVA-BC-E03-R02`. Store the record in the operator-controlled private source-of-truth repository as a committed, append-only Git artifact. Retain it for at least **24 months** or longer where an applicable project retention rule requires it.

Use this minimum record:

```text
package_id:
episode:
requested_action: publish / schedule / production-config-change / approval-only
requested_platforms:
repository:
branch:
base_sha:
final_head_sha:
changed_files:
final_video_filename:
final_video_sha256:
final_audio_filename:
final_audio_sha256:
final_asset_creation_timestamp_pacific:
final_asset_creation_timestamp_utc:
source_reference_bindings:
  - repository / branch / commit SHA / file path / file SHA-256
scene_registry_binding:
openai_audit_evidence_path:
openai_audit_evidence_sha256:
qa_result:
known_findings:
rollback_plan:
operator_approval:
  approved_by: VETS / NOT APPROVED
  approval_reference: exact VETS message, ticket, or signed approval ID
  approval_timestamp_pacific:
  approval_timestamp_utc:
  approved_action:
  approved_artifact_sha256:
```

## Mandatory Gate

Do not execute a live production mutation unless all of the following are true:

| Gate | Requirement |
|---|---|
| Exact assets | The approval record’s final asset SHA-256 values match the files about to be posted or changed. |
| Exact source | The final source head SHA and all required reference bindings match the audited evidence. |
| Audit state | The exact final artifact has a non-secret audit evidence package. Any source or asset change after review makes the audit stale. |
| Findings | No unresolved critical/high finding exists. No unresolved medium finding affects production integrity, authorization, secrets, authentication, data loss, arbitrary execution, or payments unless VETS explicitly accepts it in the record. |
| Authorization | `approved_by: VETS`, the exact approved action, and the exact matching final artifact SHA-256 are recorded. |
| Rollback | A platform-safe rollback action is documented before mutation. |

If any gate is absent or mismatched, return `HUMAN_REVIEW_REQUIRED` or `AUDIT INCOMPLETE` and do not publish/schedule/change production state.

## Verification Procedure

1. Calculate a SHA-256 checksum immediately before the intended production mutation.
2. Compare it mechanically against the checksum in `approval-record.md`.
3. Compare the final source HEAD and binding records against the audit evidence.
4. Confirm the operator approval explicitly names the action and artifact checksum.
5. Record the verification timestamp in Pacific and UTC.
6. Execute the approved single action only; do not infer permission for additional platforms or future episodes.
7. Record the action result, immutable platform post ID/URL where applicable, and rollback status in the same evidence folder.

## Rollback Baseline

Document a rollback that is proportionate to the action. For a scheduled post, cancel the schedule. For a published post, unpublish/remove only with a separate explicit VETS authorization unless the original approval record grants that narrow rollback authority. For a configuration change, restore the exact prior committed configuration.

## Evidence Privacy

Do not include secrets, private credentials, private URLs, cookies, passwords, API responses with credentials, customer data, or private messages beyond a minimal approval reference. Store only the minimum evidence necessary to reproduce the decision.

## Example Status

```text
OVERALL STATUS: HOLD
PRODUCTION AUTHORIZATION: HUMAN_REVIEW_REQUIRED
REASON: Approval record does not yet bind VETS GO to the final video SHA-256.
NEXT ACTION: Record explicit VETS approval against the exact final asset checksum, then rerun the pre-mutation verification.
```
