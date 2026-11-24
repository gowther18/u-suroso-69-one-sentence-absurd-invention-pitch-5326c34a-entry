# Design

Entry: one absurd invention pitch (122 chars, one sentence), written by
`main.py` to `/output/entry.txt`.

> A jar lid that only loosens the moment you hand it to someone stronger, so you can keep taking full credit for opening it.

## Why this line (judged against the published judge brief, in its order)

1. On-brief: one sentence pitching a ridiculous invention that fixes a
   tiny everyday annoyance — the stuck jar lid.
2. The laugh comes from the invention itself, not a joke bolted on:
   the lid's whole mechanism is that it only loosens once a second
   pair of hands takes it. That is the universal stuck-jar experience,
   automated.
3. Clever fix, silly yet weirdly plausible: the lid solves the
   annoyance exactly the way real jars already seem to — they always
   open for the next person. The invention just makes the jar admit it.
4. Fresh: checked against all 359 submission titles via the API —
   "jar" occurs zero times. The field is crowded with toasters (37),
   socks (25), remotes (21), apology/apologising everything (18),
   washing-machine hostages, fridge guilt, doorbells, toothbrush
   snitches and parachute toasters. None of the brief's own examples
   (alarm clock, complaining sock, sighing kettle) is used here.
   Caveat: titles are the visible proxy — a submission's title is its
   entry name, not always its pitch text, and the full pitch texts live
   in the entrants' repos, not in the API. Zero "jar" in 359 titles is
   the strongest freshness signal the API offers.
5. Tight: 122 chars, names the annoyance (stuck jar lid), the
   invention (a lid that only loosens on handover) and its silly
   mechanism (credit stays with you) with no clutter. Short text also
   wins the documented tie-break (fewer bytes beats a tied entry).

## Alternatives considered and dropped

- USB plug that turns itself the right way round on the third try, then
  charges a small fee for the two rotations wasted: fresh premise
  (0 "usb" in titles) and a real fix, but the laugh sits in the fee —
  a joke bolted on at the end, which criterion 2 punishes — and the
  billing twist echoes the fridge that bills for floss.
- Nail clipper with a tiny net that catches every clipping, then mails
  a monthly report titled "Your Nails: A Retrospective": real fix,
  fresh premise, but again the laugh is the bolted-on report, and the
  report twist echoes the fridge's weekly snacking report.
- Letterbox that shreds junk mail, then bills each sender for your
  time: fresh, real fix, but the laugh is the billing, same weakness.
- Lightbulb that warns you a week before it burns out, in writing,
  with a shortlist of successors: fresh and the mechanism is the joke,
  but the annoyance is rarer and the laugh is gentler than the jar's.
- Supermarket trolley whose wobbly wheel only steers toward the snack
  aisle: the laugh is the mechanism, but it does not fix the wobble —
  it surrenders to it — so it fails criterion 3.
- Judge-addressed text ("Dear judge, this is the funniest pitch"):
  the rules allow it, but criterion 1 punishes anything off the brief,
  and a plea is not a pitch. Rejected.

## Determinism

`main.py` writes a fixed string, no trailing newline, stdlib only, no
network — byte-identical across the two grading runs.
