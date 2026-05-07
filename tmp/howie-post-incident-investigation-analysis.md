# Howie Post-Incident Investigation — Structural Analysis

## Roles

### Investigator

- **Purpose:** Own the incident investigation from initial analysis through distribution of findings, ensuring a thorough and blame-aware examination of the event.
- **Domain:**
  - Investigation process and timeline
  - Calibration document
  - Final incident report
  - Interview schedule and sequencing
- **Accountabilities:**
  - Accepting and owning investigation assignments
  - Collecting and reviewing incident data (chat transcripts, logs, alert data, on-call schedules)
  - Tagging and annotating incident data to organize the analysis
  - Creating narrative timelines of the event from multiple points of view
  - Identifying and sequencing interviewees based on their involvement and knowledge
  - Conducting or co-leading interviews with incident participants
  - Writing and distributing the calibration document prior to the review meeting
  - Facilitating the learning review meeting
  - Writing the final "how we got here" incident report
  - Integrating feedback from participants into the report
  - Distributing findings across the organization

---

### Scribe

- **Purpose:** Support the investigator during interviews by accurately capturing participant answers, freeing the interviewer to focus on listening and follow-up questions.
- **Domain:**
  - Interview notes during a session
- **Accountabilities:**
  - Recording participant answers during interviews
  - Suggesting follow-up questions to the lead investigator over chat
  - Reviewing earlier discussion points as the interview progresses

---

### Incident Participant

- **Purpose:** Provide firsthand accounts, tacit knowledge, and expert perspective about the incident to support a complete and accurate investigation.
- **Domain:**
  - Their personal experience and memory of the incident
- **Accountabilities:**
  - Recounting their experience and actions during the incident when interviewed
  - Reviewing calibration documents for technical accuracy and fair representation
  - Attending and contributing to the learning review meeting
  - Providing feedback on investigation findings and the final report

---

### Subject Matter Expert

- **Purpose:** Provide specialized technical knowledge about systems or components involved in the incident to support accurate diagnosis and organizational learning.
- **Domain:**
  - Their area of technical expertise and system ownership
- **Accountabilities:**
  - Explaining how specific systems or components function
  - Validating or invalidating hypotheses about incident causes
  - Providing historical context about systems and past incidents

---

### Stakeholder

- **Purpose:** Represent business, customer, or cross-team interests in the incident and ensure findings reach relevant parts of the organization.
- **Domain:**
  - Business impact assessment and customer communication
- **Accountabilities:**
  - Attending the learning review meeting
  - Receiving and reviewing the incident report
  - Providing updates to customers or leadership during and after the incident

---

## Artifacts

### Calibration Document

- **Format:** Digital
- **Description:** An interim findings document created by the investigator and shared with participants before the learning review meeting to ensure alignment and prevent surprises during the meeting.
- **Parts:**
  - `Artifact::part` — Data reviewed to date (transcripts, interviews, logs consulted)
  - `Artifact::part` — List of interviewees and their roles
  - `Artifact::part` — Emerging themes from the investigation
  - `Artifact::part` — Open questions to be discussed at the meeting

---

### Incident Report ("How We Got Here" Report)

- **Format:** Digital
- **Description:** The final organizational record of the incident, telling the narrative story of how the event unfolded from multiple perspectives; focused on learning rather than corrective action.
- **Parts:**
  - `Artifact::part` — Narrative of the event from multiple participant perspectives
  - `Artifact::part` — Technical background and system history relevant to the event
  - `Artifact::part` — Contributing factors and key themes
  - `Artifact::part` — Timeline visualization
  - `Artifact::part` — Action items and follow-up work

---

### Timeline

- **Format:** Digital
- **Description:** A visual representation of the incident's progression, created in multiple forms to surface different viewpoints and key moments beyond a simple chronological sequence.
- **Parts:**
  - `Artifact::part` — Point-of-view timelines (one per participant perspective)
  - `Artifact::part` — Narrative timeline (key moments, hypotheses raised/disproved, escalations, resolution)

---

### Interview Notes

- **Format:** Digital
- **Description:** Notes captured during investigator interviews with incident participants, including answers, quoted statements, thematic observations, and follow-up items.
- **Parts:**
  - `Artifact::part` — Participant answers and direct quotes
  - `Artifact::part` — Themes identified during the session
  - `Artifact::part` — Remaining questions and follow-up items

---

### Tags

- **Format:** Digital
- **Description:** Annotations applied to incident data (chat transcripts, logs) to categorize and organize key events; the primary mechanism for structuring the initial analysis.

---

### Action Items List

- **Format:** Digital
- **Description:** A list of follow-up tasks and countermeasures generated during the investigation and review meeting, assigned to responsible parties with agreed timelines.

---

### Post-Meeting Survey

- **Format:** Digital
- **Description:** A brief two-to-four-question survey circulated after the learning review meeting to capture participant feedback on the meeting process and the investigation findings.

---

## Meetings

### Learning Review Meeting

- **Requirement documents:**
  - Calibration document (shared with participants in advance)
  - Narrative timeline
  - Interview notes and supporting materials (screenshots, recordings)
- **Participants:** Incident responders who were involved in detection, diagnosis, or resolution; subject matter experts on affected systems; dependent service teams; engineers from related but unimpacted parts of the business; impacted users; customer success roles; management; key stakeholders — open to anyone interested.
- **Agenda items:**
  - `Meeting::agenda-item` — Intro and opening remarks: set ground rules, explain blame-aware framing, confirm recording consent
  - `Meeting::agenda-item` — Overview of artifacts studied and methods used in the investigation
  - `Meeting::agenda-item` — Interactive narrative walkthrough of the incident with participant input
  - `Meeting::agenda-item` — Background knowledge session: subject matter expert explains relevant systems
  - `Meeting::agenda-item` — Themes review and commentary from participants (two to five themes)
  - `Meeting::agenda-item` — Discussion of unresolved questions
  - `Meeting::agenda-item` — Summary of what has been done so far
  - `Meeting::agenda-item` — Next steps and scheduling of the action items meeting
- **Output documents:**
  - Refined incident findings (incorporated into the final report)
  - Action items list
  - Meeting recording (optional)
- **Meeting::Role:**
  - `Facilitator` ← derived from `Investigator`
  - `Expert Presenter` ← derived from `Subject Matter Expert`
  - `Contributor` ← derived from `Incident Participant`

---

### Action Items Meeting

- **Requirement documents:**
  - Learning review findings
  - Action items list from the investigation and review meeting
- **Participants:** Team owners of affected systems; product owners; engineering managers; project managers — those who will own and execute the follow-up work.
- **Agenda items:**
  - `Meeting::agenda-item` — Review of action items raised during the investigation and learning review
  - `Meeting::agenda-item` — Assignment of ownership to responsible parties
  - `Meeting::agenda-item` — Agreement on timelines and formats for completion
- **Output documents:**
  - Work tickets (e.g., Jira)
  - Assigned action items with owners and agreed timelines
- **Meeting::Role:**
  - `Facilitator` ← derived from `Investigator`
