---
Title: A One-Year Self-Reflection on scikit-learn
date: 2026-03-14
slug: scikit-learn-one-year-self-reflection
category: blog
tags: open-source contribution, scikit-learn, self-reflection
summary: Reflections on one year of working with the scikit-learn team.
---

*Disclosure: I used ChatGPT to proofread earlier drafts of this blog post.*

It's been a year since I joined the scikit-learn team, so I decided to write a blog
post to document some of my thoughts.

---

### Why Did I Stay in scikit-learn?

I have had a great experience working with the scikit-learn community. When I first
started, I knew very little about programming and software development. Because of
that, the absence of certain computer science and engineering common sense created
quite a few awkward situations when working with the maintainers.

The maintainers did not mind this and patiently mentored me, helping me understand
the contribution workflow and the code base. This mentorship helped me learn new
skills and boosted my confidence, which motivated me to take on more responsibilities
in the community, such as reviewing pull requests and triaging issues.

Moreover, I realised that it is possible to transform challenges into situations
where everyone wins, which I find extremely rewarding and fulfilling.

Furthermore, I have the opportunity to work with a fantastic group: the
scikit-learn team.

### What Did I Do?

I received the invitation to join the scikit-learn team in December 2024. Prior to
this, I was already engaging with the community by authoring pull requests, reviewing
other contributions, and participating in issue triaging.

Over the past year, I have contributed to documentation improvements, feature
development, and community processes. I have also participated in reviewing pull
requests and helping first-time contributors navigate the project. One of the
features I later helped implement was temperature scaling for probability
calibration, which will be available in scikit-learn 1.8 (See my 
[previous blog post]({filename}/blog/20250802-scikit-learn-temperature-scaling.md)
on it).

Some examples of my involvement before joining the team include:

1. [<code>scikit-learn/scikit-learn/27913</code>: Added link to plot_adaboost_multiclass.py example](https://github.com/scikit-learn/scikit-learn/pull/27913)

    My first pull request for scikit-learn.
    [Maren Westermann](https://github.com/marenwestermann)
    helped me navigate the codebase and understand the CI workflow, which gave me a
    solid foundation for later contributions. Even though I am now more experienced
    with the contributing workflow, I still revisit that PR from time to time to
    remind myself how to support first-time contributors.

2. [<code>scikit-learn/scikit-learn/29709</code>: ENH add support for array API to various metrics](https://github.com/scikit-learn/scikit-learn/pull/29709)

    My first involvement with scikit-learn's
    [array API project](https://scikit-learn.org/stable/modules/array_api.html),
    which quickly became a mid-term goal for my work in the project.

3. [<code>scikit-learn/scikit-learn/30059</code>: DOC fix back references to removed example](https://github.com/scikit-learn/scikit-learn/pull/30059)

    One of the first pull requests I reviewed for scikit-learn. Together with
    [Guillaume Lemaitre](https://github.com/glemaitre)
    and
    [Charlie Xiao](https://github.com/Charlie-XIAO),
    we fixed a bug on the scikit-learn website. From reporting the issue on the
    tracker, analysing the root cause, creating a patching pull request, and merging
    it into the `main` branch, the entire process took less than an hour.

4. [<code>scikit-learn/scikit-learn/30076</code>: Error on the scikit-learn algorithm cheat-sheet?](https://github.com/scikit-learn/scikit-learn/issues/30076)

    One of the first scikit-learn issues I helped triage.

#### Creating Pull Requests

I originally learned programming by working on online problem sets. When I was
working on
[<code>scikit-learn/scikit-learn/27913</code>](https://github.com/scikit-learn/scikit-learn/pull/27913),
I had no idea what linting was. I saw the GitHub Actions bot's warning and a large
cross in the CI/CD workflow, but I did not know how to address the issue, or even
whether I needed to.
[Maren](https://github.com/marenwestermann)
spent a lot of time helping me navigate the codebase and understand the CI/CD
messages, and the PR was eventually merged into the `main` branch.
The merge boosted my confidence and motivated me to actively search for other issues
where I could help. This led me to
[<code>scikit-learn/scikit-learn/29709</code>](https://github.com/scikit-learn/scikit-learn/pull/29709).

It was reported that the input validation logic in both
[<code>sklearn.metrics.root_mean_squared_log_error</code>](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html)
and
[<code>sklearn.metrics.mean_squared_log_error</code>](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error)
was supposed to check whether the inputs lie inside the domain of
$y = \log(1 + x)$. However, the implementation at that time was checking
$y = \log(x)$ instead.
This turned out to be one of the relatively few issues in scikit-learn that I was
able to solve. I commented on the issue thread to confirm the problem and volunteered
to work on it.
[Adrin](https://github.com/adrinjalali)
provided the first round of review. Because the fix was relatively straightforward,
it did not take long for him to give the initial approval. He then asked me to add
support for the
[array API](https://scikit-learn.org/stable/modules/array_api.html)
to those functions.

At that time, I had no idea what the
[array API](https://scikit-learn.org/stable/modules/array_api.html)
was. From the merged PR, it seemed that the objective was simply to replace the
NumPy abbreviation `np` with a more abstract term `xp`. However, I did not understand
what this change meant for the scikit-learn codebase or why it was an objective.
I looked up the meta-issue
[<code>scikit-learn/scikit-learn/26024</code>](https://github.com/scikit-learn/scikit-learn/issues/26024),
which helped a little. Fortunately, ChatGPT was available at the time, so I used it
to ask a few questions and better understand what the
[array API project](https://scikit-learn.org/stable/modules/array_api.html)
was about.
Together with
[Thomas Fan](https://github.com/thomasjpfan)'s
presentation
[<i>scikit-learn on GPUs with Array API</i>](https://www.youtube.com/watch?v=c_s8tr1AizA)
from PyData NYC 2023, I learned about the purpose of the
[array API project](https://scikit-learn.org/stable/modules/array_api.html)
and immediately became interested because I found it meaningful and impactful.

The array API project quickly became a mid-term goal for my work in scikit-learn,
and I hope to see it completed. Under the mentorship of
[Adrin Jalali](https://github.com/adrinjalali),
[Olivier Grisel](https://github.com/ogrisel),
and
[Omar Salman](https://github.com/OmarManzoor),
[<code>scikit-learn/scikit-learn/29709</code>](https://github.com/scikit-learn/scikit-learn/pull/29709)
was successfully merged into the `main` branch, and my future PRs gradually improved.

#### Reviewing Pull Requests

From
[Adrin](https://github.com/adrinjalali)
during the Code 4 Thought interview
[<i>scikit-learn: Software is People</i>](https://www.youtube.com/watch?v=dMbWkAosBVA),
I learned that every scikit-learn PR requires two approvals.
This helped me realise that contributors can support the project not only by writing
code but also by reviewing and mentoring others.

At that time, I was still familiarising myself with the project standards and the
contributing workflow, so I cherry-picked some simpler PRs to review. Fortunately,
[Adrin](https://github.com/adrinjalali)
was managing the meta-issue
[<code>scikit-learn/scikit-learn/26927</code>](https://github.com/scikit-learn/scikit-learn/issues/26927),
which aimed to onboard first-time contributors.
Having gone through the same process while working on
[<code>scikit-learn/scikit-learn/27913</code>](https://github.com/scikit-learn/scikit-learn/pull/27913),
I was able to provide constructive feedback to other first-time contributors by
mimicking the feedback I had received from
[Maren](https://github.com/marenwestermann)
and
[Adrin](https://github.com/adrinjalali).

Another PR I helped review was
[<code>scikit-learn/scikit-learn/30059</code>](https://github.com/scikit-learn/scikit-learn/pull/30059).
It was reported that a broken image appeared on the scikit-learn website because
some examples had been removed in a previously merged PR. Together with
[Guillaume Lemaitre](https://github.com/glemaitre)
and
[Charlie Xiao](https://github.com/Charlie-XIAO),
we resolved the issue, from identifying the root cause to creating a fix and merging
the PR within an hour.

This kind of collaboration created a strong sense of accomplishment and encouraged
me to become more involved in the community, not only by creating PRs but also by
reviewing them and participating in issue triaging.
This created opportunities for me to interact regularly with both the core
maintainers and the wider community.

---

### The Future

I would like to see the completion of array API support in scikit-learn, and I know
the best way to help achieve this is to stay actively involved in the project.
Thanks to the tremendous work of
[Olivier Grisel](https://github.com/ogrisel),
[Omar Salman](https://github.com/OmarManzoor),
[Tim Head](https://github.com/betatim),
[Lucy Liu](https://github.com/lucyleeow),
and many other contributors, the project is progressing rapidly.
Many scikit-learn estimators and functions now support GPU-backed arrays, with
additional support on the way.

I would also like to become more involved in the CI/CD processes of the project,
as well as the public release workflow.

---

### Conclusion

In the Code 4 Thought interview
[<i>scikit-learn: Software is People</i>](https://www.youtube.com/watch?v=dMbWkAosBVA),
[Gael Varoquaux](https://github.com/GaelVaroquaux)
mentioned that he believes diversity of opinion leads to better software. scikit-learn
demonstrates this principle well. When collaborating, the team consistently prioritises
the long-term interests of the project—such as maintainability, numerical stability,
and backward compatibility—over personal ambition or ego.

This is a quality I deeply admire. I am grateful that the team welcomed me and
trusted me with greater responsibilities, and I look forward to continuing to
contribute to the project and the community in the years ahead.