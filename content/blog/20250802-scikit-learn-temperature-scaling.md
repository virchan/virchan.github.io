---
Title: Temperature Scaling in Scikit-Learn
date: 2025-08-02
slug: scikit-learn-temperature-scaling
category: blog
tags: open-source contribution, probability calibration, scikit-learn
summary: A summary of my scikit-learn pull request on temperature scaling.
---

The temperature scaling PR, 
[<code>scikit-learn/scikit-learn/31068</code>](https://github.com/scikit-learn/scikit-learn/pull/31068), 
that [Christian Lorentzen](https://github.com/lorentzenchr) and I worked on has finally
been merged into scikit-learn's main branch. Probability calibration with temperature 
scaling will be available in scikit-learn 1.8.

I'd like to thank 
[Olivier Grisel](https://github.com/ogrisel), 
[Christian Lorentzen](https://github.com/lorentzenchr), 
and [Omar Salman](https://github.com/OmarManzoor)
for guiding me through the entire process. For every minute I spent working on the PR, 
they spent hours reviewing to ensure algorithmic efficiency, numerical stability, 
correct unit tests, and rigorous documentation. I'd also like to thank 
[David Holzmüller](https://github.com/dholzmueller) 
for his hard work in convincing the scikit-learn core maintainers that temperature 
scaling is a valuable addition to the library --- the merge wouldn't have been 
possible without him --- and to 
[Adrin Jalali](https://github.com/adrinjalali) 
for his confident vote to let me open the PR.

---

### How It Started

Suppose we are working on a multi-class classification problem. For a given sample, let 
$z$ be the vector of logits for each class as predicted by the estimator to be 
calibrated (i.e., the output of `decision_function` or `predict_proba`). Temperature 
scaling produces class probabilities by modifying the softmax function with a 
temperature parameter $T$:

$$\mathrm{softmax}\left( \frac{z}{T} \right).$$

In particular, probabilities are converted to logits by first adding a tiny positive 
constant to avoid numerical issues with taking the logarithm of zero, and then 
applying the natural logarithm.

It was suggested in 
[<code>sklearn/sklearn/28574</code>](https://github.com/scikit-learn/scikit-learn/issues/28574) 
to include temperature scaling in 
[<code>CalibratedClassifierCV</code>](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#calibratedclassifiercv). 
According to 
[scikit-learn's FAQ](https://scikit-learn.org/stable/faq.html), 
a rule of thumb for including a new algorithm is:

* at least 3 years since publication,  
* 200+ citations,  
* wide use and usefulness.  

For temperature scaling, the only hurdle was to justify the "usefulness" part of the 
third criterion --- this was eventually settled by Holzmüller and his collaborators, 
who benchmarked its performance on calibrating XGBoost and neural networks. 
(This is well documented in the discussion in 
[<code>sklearn/sklearn/28574</code>](https://github.com/scikit-learn/scikit-learn/issues/28574), 
so I won't repeat it here.) Because the effect of temperature scaling on non-neural 
models was new, the core developers welcomed the benchmarking and agreed to include it.

I had always wanted to contribute something substantial to the scikit-learn community 
and improve my software/machine learning engineering skills. Since I had participated 
in the discussion from the start and built a good reputation among the core developers 
through earlier contributions, they gave me the go-ahead to create the PR.

---

### What Did I Learn?

#### Documentation Is as Important as the Code Itself

This is strongly encouraged in 
[scikit-learn's Contributing Guide](https://scikit-learn.org/stable/developers/contributing.html). 
I've learned first-hand that optimised code is often difficult to follow. For example, 
one property of temperature scaling is that the accuracy score of the calibrated model 
should remain unchanged. However, my early unit tests couldn't reproduce this. I 
suspected Python's floating-point handling, or a bug in SciPy's 
[<code>minimize_scalar</code>](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html#scipy.optimize.minimize_scalar), 
but the real cause was the $k$-fold cross-validation used in 
[<code>CalibratedClassifierCV</code>](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#calibratedclassifiercv). 
As it turned out, this behaviour was documented --- which I discovered only after weeks 
of trial and error.

From this, I learned that good documentation doesn't just describe expected behaviour; 
it also makes it easier for future developers to update the code. I kept this in mind 
when writing the user guide and documentation for temperature scaling.

#### Reviewers Are Allies

Every scikit-learn PR requires at least two reviewers' approval. With 
[<code>scikit-learn/scikit-learn/31068</code>](https://github.com/scikit-learn/scikit-learn/pull/31068), 
it was common for me to push commits before bed and wake up to 20+ comments. Far from 
being overwhelmed, I found this exciting.

Why? First, I always learned something --- whether about project standards, the 
codebase, or the software engineering aspects like computational efficiency and 
numerical stability. Second, my reviewers clearly invested significant time in 
reading my work. Their comments were precise, concise, and well-structured, even when 
explaining complex theoretical and engineering issues. This made me want to match or 
exceed their level of quality in my responses.

#### Patience and Persistence

The PR was opened in March 2025 and merged in August. Over those five months, there was 
a lot of back-and-forth. Addressing reviewer feedback sometimes took time.

For example, we decided the API should raise an error if 
[<code>minimize_scalar</code>](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html#scipy.optimize.minimize_scalar) 
terminated unsuccessfully, and we needed a unit test for this. I spent weeks trying to 
create an example to trigger such a termination, but eventually realised it was 
impossible --- any such example would trigger an error earlier in a private function 
before the optimiser ran.

When I reported this, my reviewers also needed time to consider it. I was mindful that 
they have other responsibilities and that complex issues take time to think through. I 
preferred to wait patiently so that everyone understood the reasoning, rather than 
rushing to merge and risking confusion later.

---

### Some Final Thoughts

The temperature scaling PR is one of my biggest projects of 2025, and I'm thrilled it's 
now part of scikit-learn. It's been a deeply meaningful experience for my personal and 
professional growth --- something I had been seeking since graduating. I'm grateful to 
the scikit-learn community, especially the core contributors, who patiently mentored me 
from the ground up and trusted me to implement this important feature.

One last thought: I felt a bit empty after the merge. The clock is striking thirteen, 
so I suppose it's time to head back to the issue tracker --- either to triage or help 
review other PRs.