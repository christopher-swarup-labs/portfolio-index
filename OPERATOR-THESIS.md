# Operator Thesis

> **Evidence classification:** Original operator thesis, informed by repeated professional experience and written specifically for this portfolio.

What I believe about how B2B revenue systems actually work, and why I build them the way I do.

---

## 1. Most GTM problems are ownership problems wearing a data costume

The presenting complaint is almost always a number. Attribution is wrong. MQL volume is up and pipeline is flat. The forecast missed again. Teams then buy a tool aimed at the number.

The number is rarely the fault. Underneath a broken attribution report is usually an unresolved question about who owns a record at each point in its life, and what the organisation has agreed a stage means. Two teams operating different definitions of "qualified" will produce irreconcilable reporting no matter which platform generates it. Fix the ownership and definition layer and a surprising amount of the reporting problem dissolves without new software.

This is why my first move on any engagement is a lifecycle and authority map, not a tool audit.

## 2. A lifecycle model is a political artefact before it is a technical one

Lifecycle design fails when it is treated as configuration. The hard part is not building the stages — it is getting Marketing, SDR leadership, Sales and Customer Success to accept a definition that costs each of them something.

An operator who cannot hold that conversation will ship a technically elegant model that the organisation quietly routes around. I have watched well-built lifecycle rebuilds die because nobody secured the SDR leader who lost discretion over what counts as a real lead.

So the design work and the stakeholder work are the same work. A lifecycle model with no named accountable owner per stage, and no agreed exception path, is a diagram.

## 3. Reporting credibility is a finite resource

An operations function gets a limited number of chances to present a number that a CRO later finds to be wrong. Spend them and the function is relegated to execution regardless of the quality of its thinking.

The practical consequence is that I would rather ship a narrower report I can defend line by line than a comprehensive one with a soft centre. That means being explicit about what is measured, what is inferred, what is modelled, and what is simply not known. Separating fact from inference is not academic caution — it is how an operations leader retains the standing to be believed on the next hard call.

## 4. Automate the decision only after you can articulate the decision

Automation encodes a decision. If the decision is not clearly articulated, automation encodes an ambiguity and then executes it thousands of times per day at a speed that makes it hard to detect.

Routing is the clearest example. Routing logic is where an organisation's unresolved arguments about territory, ownership and account definition go to hide. Automating it before those arguments are settled does not settle them; it buries them in rules nobody can read.

The same holds one level up for AI. Which brings me to the point I care most about.

## 5. AI raises the cost of a weak operating foundation

The prevailing framing is that AI compensates for operational immaturity — that a sufficiently capable model can reason its way past bad data and unclear process.

My experience points the other way. AI applied to a trustworthy foundation compounds its value. AI applied to a contested one produces output that is fluent, fast, confidently wrong, and much harder to challenge than a spreadsheet, because it arrives without visible workings. The failure mode is not that the AI is wrong. It is that nobody can tell it is wrong until a quarter has been planned on it.

The operating implication is a sequence, not a prohibition:

1. Agree ownership and decision rights.
2. Fix definitions and the data that expresses them.
3. Make the decision logic explicit and inspectable.
4. Then automate, keeping evidence, assumptions and uncertainty visible in the output.
5. Keep a named human accountable for anything that moves money or headcount.

Point 4 is the one most organisations skip. An AI-assisted operations output that does not distinguish between what it observed, what it assumed, and what it recommends is not a productivity tool — it is a liability with good formatting.

## 6. Operations should be designed for adoption, not for correctness

A correct process that nobody follows has a value of zero, and a negative value if it is reported on as though it were followed.

I design intake, enablement and exception handling as first-class parts of a system rather than as a rollout afterthought. The test of a lifecycle model is not whether it is coherent on a diagram. It is whether an SDR under quota pressure at 4pm on the last day of the month can follow it, and whether the exception they need exists as a designed path rather than an improvisation.

## 7. The reusable asset is the diagnostic, not the answer

Every organisation's GTM system is idiosyncratic. What transfers between them is not the solution — it is the sequence of questions that locates the real fault, and the ability to recognise a symptom pattern quickly.

That is the thesis behind the structured operator skills catalogued in `SKILLS-AND-SYSTEMS.md`: encoding diagnostic sequence, evidence standards and human accountability boundaries, so that judgement is applied consistently rather than re-derived. It is also the thesis behind any productisation of this work — the durable value sits in the diagnostic logic and the operating standards, not in a specific configuration.

---

## What would change my mind

On point 5 in particular: if AI-assisted GTM tooling matures to the point where models reliably surface their own uncertainty and refuse to answer on insufficient evidence, the sequencing argument weakens considerably. That would be a good outcome, and I would rather be wrong about it than right.

I hold points 1 through 4 with high confidence, drawn from repeated pattern across seven organisations. Point 7 is the least tested — it is a bet about transferability that the skills library exists to prove or disprove.
