# 📄 Resume Bot - Project Requirements Document (PRD)

## Requirements Table

| Requirement ID | Description | User Story | Expected Behavior/Outcome |
|----------------|-------------|------------|----------------------------|
| DB-01 | Store user background (experience, education, skills, tech stack) in a vector database | As a user, I want to input my professional background so the bot can use it to customize my resume for each job | User data is embedded and stored for future semantic matching |
| DB-02 | Perform semantic search for keyword and experience matching | As a system, I want to find relevant information from the vector DB when tailoring resumes | Relevant keywords and experience are injected into the resume when required by a JD |
| NAV-01 | Load job application websites from bookmarks or hardcoded URLs | As a user, I want the bot to visit job sites automatically without manual input | Bot launches and navigates job application websites autonomously |
| JD-01 | Parse job descriptions from each visited site | As a system, I want to read the job descriptions like a human reader | Job descriptions are fully read and understood |
| JD-02 | Evaluate job fit using a relevance metric | As a system, I want to assess job listings based on closeness to user’s resume focus | Bot applies only to relevant jobs (e.g., Fullstack, Frontend), skips irrelevant ones |
| JD-03 | Handle edge cases (e.g., borderline job matches) | As a user, I want the bot to ask for confirmation before applying to unrelated or borderline listings | Bot skips or requests user confirmation (planned for future release) |
| RS-01 | Add missing keywords to resume if relevant | As a system, I want to enhance resumes by adding relevant terms from the JD | Bot injects matching tech terms (e.g., “Zustand” if similar to “Redux”) |
| RS-02 | Add missing experience if relevant | As a system, I want to inject relevant experience examples from DB when JD requires them | Resume is updated with relevant achievements/experiences |
| RS-03 | Ensure resume does not exceed one page | As a user, I want to make sure my resume stays within one page even after edits | Resume is trimmed automatically while keeping most relevant content |
| RS-04 | Preview resume before submission | As a user, I want to see the updated resume before it gets submitted | A final preview of the tailored resume is shown |
| APP-01 | Automatically submit the tailored resume | As a user, I want the bot to complete the job application after tailoring the resume | Resume is submitted without user interaction |
| FLOW-01 | Repeat the process for multiple job listings on one site | As a user, I want the bot to apply for all suitable jobs on a given website | Bot processes all listings on a website sequentially |
| FLOW-02 | Move to the next job website when one is done | As a user, I want the bot to apply across multiple platforms | Bot finishes one site and moves on until all are done |
| FLOW-03 | Complete full application session | As a user, I want the bot to stop after all applications are submitted | Bot ends when the entire workflow is complete |
