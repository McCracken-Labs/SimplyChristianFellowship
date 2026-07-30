# Simply Christian Fellowship — Blog & Devotional Plan

A weekly Sunday post in two parts: a short **devotional** (opening scripture, a reflection, one small practice, and a closing blessing) followed by a longer **reflection essay** on the same theme. Every post stands on its own, and together the 52 weeks walk through the teachings of Jesus and circle back to where the site begins: only Christ is holy, and to follow Him is simply to love.

Scripture uses the King James Version and the American Standard Version (both public domain), or original renderings, per the devotional build standards. Cadence rules from the book instructions apply to every entry: no em dashes, no rule-of-three morals, no mirrored contrasts, plain and human.

## How publishing works

- Posts live in `/blog/` as individual pages. `blog/posts.json` is the manifest for all 52 weeks.
- `build_blog.py` regenerates the archive (`blog/index.html`) and the RSS feed (`feed.xml`), showing only posts whose Sunday has arrived. Future weeks stay hidden until their date.
- A GitHub Action (`.github/workflows/publish.yml`) runs every Sunday and republishes, so each week's post goes live and enters the RSS feed on its own.
- A newsletter service set to RSS-to-email watches `feed.xml` and emails subscribers when a new item appears. (Service still to be chosen.)
- Week 1 is published now as the launch post. Weeks 2 to 52 are written ahead of time and scheduled; each appears on its Sunday.

## Optional: a daily devotional

The 52 weekly devotionals can later be expanded into a full daily devotional and built into a 6x9 print book and ebook using the devotional build instructions. That is a separate project once the weekly rhythm is running.


## Foundations

**Week 1 — Only Christ Is Holy**  ·  Aug 2, 2026  ·  _Luke 18:19_  
No book, building, or person is holy in itself. Holiness belongs to God, and came near in one person.

**Week 2 — Scripture as a Window, Not an Idol**  ·  Aug 9, 2026  ·  _John 5:39-40_  
The Bible points to Christ. Some end up worshipping the pages instead of following the person they describe.

**Week 3 — To Follow Is Simply to Love**  ·  Aug 16, 2026  ·  _John 13:34-35_  
The heart of the whole thing, and the tagline of this fellowship.

**Week 4 — The Two Commands That Hold Everything**  ·  Aug 23, 2026  ·  _Matthew 22:37-40_  
Love God, love your neighbor. Jesus said all the rest hangs on these.

**Week 5 — Who Jesus Said He Was**  ·  Aug 30, 2026  ·  _John 14:6_  
Not a philosophy or a rulebook. A person to follow.

**Week 6 — The Beatitudes**  ·  Sep 6, 2026  ·  _Matthew 5:3-10_  
Jesus blesses the poor, the mourning, the meek, the merciful. The kingdom turned upside down.

**Week 7 — Salt and Light**  ·  Sep 13, 2026  ·  _Matthew 5:13-16_  
Faith is meant to be tasted and seen, not hidden.

**Week 8 — Turn the Other Cheek**  ·  Sep 20, 2026  ·  _Matthew 5:38-42_  
The hardest, plainest teaching about how to answer harm.

**Week 9 — Love Your Enemies**  ·  Sep 27, 2026  ·  _Matthew 5:43-48_  
Anyone can love a friend. Christ asks for more.

**Week 10 — Give in Secret**  ·  Oct 4, 2026  ·  _Matthew 6:1-4_  
Real giving does not need an audience.

**Week 11 — How to Pray Simply**  ·  Oct 11, 2026  ·  _Matthew 6:5-13_  
Jesus gave a short, plain prayer and warned against showy ones.

**Week 12 — Do Not Worry**  ·  Oct 18, 2026  ·  _Matthew 6:25-34_  
A word for anxious hearts about trust and enough.

**Week 13 — Judge Not**  ·  Oct 25, 2026  ·  _Matthew 7:1-5_  
Deal with your own heart before you weigh anyone else's.


## The Way of Love

**Week 14 — The Good Samaritan**  ·  Nov 1, 2026  ·  _Luke 10:25-37_  
The neighbor is whoever is bleeding in the road in front of you.

**Week 15 — Welcome the Stranger**  ·  Nov 8, 2026  ·  _Matthew 25:35_  
On immigrants, outsiders, and the ones others turn away.

**Week 16 — Feed the Hungry**  ·  Nov 15, 2026  ·  _Matthew 25:35-40_  
Christ said He is met in the hungry person we feed.

**Week 17 — The Least of These**  ·  Nov 22, 2026  ·  _Matthew 25:40_  
A whole life measured by mercy shown with the hands.

**Week 18 — Forgive Seventy Times Seven**  ·  Nov 29, 2026  ·  _Matthew 18:21-22_  
Forgiveness that refuses to keep count.

**Week 19 — The Unforgiving Servant**  ·  Dec 6, 2026  ·  _Matthew 18:23-35_  
We forgive because we have been forgiven far more.

**Week 20 — The Prodigal Son**  ·  Dec 13, 2026  ·  _Luke 15:11-32_  
A homecoming, and a love that does not wait to be earned.

**Week 21 — The Lost Sheep**  ·  Dec 20, 2026  ·  _Luke 15:3-7_  
No one is written off.

**Week 22 — Blessed Are the Merciful**  ·  Dec 27, 2026  ·  _Matthew 5:7_  
Why mercy sits at the center of the way.

**Week 23 — Let the Children Come**  ·  Jan 3, 2027  ·  _Matthew 19:14_  
The kingdom belongs to the small and the overlooked.

**Week 24 — Wash One Another's Feet**  ·  Jan 10, 2027  ·  _John 13:12-17_  
Leadership in the kingdom looks like a servant with a towel.

**Week 25 — Known by Love**  ·  Jan 17, 2027  ·  _John 13:35_  
The only badge Jesus gave His followers.

**Week 26 — Bless Those Who Curse You**  ·  Jan 24, 2027  ·  _Luke 6:27-28_  
Returning kindness for hostility.


## Money, Power, and the Kingdom

**Week 27 — Jesus Never Asked for a Tithe**  ·  Jan 31, 2027  ·  _2 Corinthians 9:7_  
Where the tithe came from, and what Christ asked for instead.

**Week 28 — The Widow's Two Coins**  ·  Feb 7, 2027  ·  _Mark 12:41-44_  
Generosity is measured by the heart, not the amount.

**Week 29 — The Camel and the Needle**  ·  Feb 14, 2027  ·  _Mark 10:23-27_  
A hard word about wealth, and the hope inside it.

**Week 30 — The Rich Fool and His Barns**  ·  Feb 21, 2027  ·  _Luke 12:16-21_  
Storing up for yourself while your neighbor goes without.

**Week 31 — You Cannot Serve Two Masters**  ·  Feb 28, 2027  ·  _Matthew 6:24_  
One heart cannot bow to both.

**Week 32 — The Tables in the Temple**  ·  Mar 7, 2027  ·  _Matthew 21:12-13_  
The one time Jesus got angry, and why.

**Week 33 — Prosperity Is Not a Promise**  ·  Mar 14, 2027  ·  _Luke 9:23-24_  
Answering the preachers who sell blessing for donations.

**Week 34 — Whoever Wants to Be Great**  ·  Mar 21, 2027  ·  _Mark 10:42-45_  
Real greatness in the kingdom is service.

**Week 35 — Render Unto Caesar**  ·  Mar 28, 2027  ·  _Matthew 22:15-22_  
Faith is not a political weapon.

**Week 36 — Not of This World**  ·  Apr 4, 2027  ·  _John 18:36_  
Jesus refused earthly power every time it was offered.

**Week 37 — The Workers in the Vineyard**  ·  Apr 11, 2027  ·  _Matthew 20:1-16_  
Grace is not fair, and that is good news.

**Week 38 — Treasure in Heaven**  ·  Apr 18, 2027  ·  _Matthew 6:19-21_  
What you store points to what you love.

**Week 39 — Sell What You Have**  ·  Apr 25, 2027  ·  _Luke 12:33_  
On loosening the grip of what we own.


## Living It Out

**Week 40 — Faith Without Works Is Dead**  ·  May 2, 2027  ·  _James 2:14-17_  
You can call yourself an astronaut, but you have to get off the ground.

**Week 41 — Not Everyone Who Says Lord**  ·  May 9, 2027  ·  _Matthew 7:21_  
Words are cheap. The Father looks at a life.

**Week 42 — Known by Their Fruit**  ·  May 16, 2027  ·  _Matthew 7:16-20_  
The proof of a faith is what it produces.

**Week 43 — The House on the Rock**  ·  May 23, 2027  ·  _Matthew 7:24-27_  
Hearing the words is not the same as living them.

**Week 44 — The Veil Was Torn**  ·  May 30, 2027  ·  _Matthew 27:50-51_  
You do not need a gatekeeper to reach God.

**Week 45 — Fellowship Without Walls**  ·  Jun 6, 2027  ·  _John 17:20-23_  
Unity that holds difference without fear.

**Week 46 — Doubt Is Welcome Here**  ·  Jun 13, 2027  ·  _John 20:24-29_  
Honest questions are not the enemy of faith.

**Week 47 — Test Everything**  ·  Jun 20, 2027  ·  _1 Thessalonians 5:21_  
Faith is not afraid of a hard question.

**Week 48 — The Heavens Declare**  ·  Jun 27, 2027  ·  _Psalm 19:1_  
Science and faith explore the same creation.

**Week 49 — Consider the Lilies**  ·  Jul 4, 2027  ·  _Matthew 6:28-29_  
Creation as a teacher of trust.

**Week 50 — Come to Me, All Who Are Weary**  ·  Jul 11, 2027  ·  _Matthew 11:28-30_  
A gentle word for the tired and the burdened.

**Week 51 — The Greatest of These Is Love**  ·  Jul 18, 2027  ·  _1 Corinthians 13:13_  
Everything else falls away. Love stays.

**Week 52 — Simply Christian**  ·  Jul 25, 2027  ·  _Micah 6:8_  
Circling back to the beginning: do justly, love mercy, walk humbly.
