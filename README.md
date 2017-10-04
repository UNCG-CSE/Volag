# Naive Bayes

Naive Bayes is a set of supervised learning algorithms based on applying Bayes' theorem with the "naive" assumption of independence between every pair of features. For example, a fruit may be considered to be an apple if it is red, round, and about 3" in diameter. A Naive Bayes classifier consider each of these "features" (color, shape, size) to contribute independently to the probability that the fruit is an apple, regardless of any correlations between features. Features, however, aren't always independent which is often seen as a shortcoming of the Naive Bayes algorithm and this is why it's labeled "naive".

Naive Bayes is very popular in text classification, and is extremely useful in common applications like spam detection and document classification.

In short, the algorithm allows us to predict a class, given a set of features using probability. Back to the fruit example, we could predict whether a fruit is an apple, orange, or banana (its class) based on its color, shape, etc (its features).

For our project, we could consider our features to be day, time, season, weather characteristics, etc. in order to predict the class of a flight - delayed vs. non-delayed.

## Naive Bayes in scikit-learn

scikit-learn provides a few different Naive Bayes algorithms that can be run easily in python.
Available algorithms:
* Gaussian Naive Bayes
    * used for data in which the likelihood of features is assumed to be Gaussian

* Multinomial Naive Bayes
    * one of the two classic Naive Bayes variants used in text classification (where the data are typically represented as word vector counts)

* Bernoulli Naive Bayes
    * used for data that is distributed according to multi-variate Bernoulli distributions
        * i.e. there may be multiple features but each one is assumed to be a binary-valued (Bernoulli, boolean) variable

We will most likely be looking at Gaussian or Multinomial Naive Bayes. The Bernoulli variant doesn't seem to be a good fit, as our features are not boolean.


## Links
[Wikipedia: Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

[scikit-learn: Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html)
