Title: Hello Phabricator
Date: 2015-06-18 17:00
Author: egig
Category: Uncategorized
Slug: hello-phabricator
Status: published

So, due to the codes that always being sucks and hard to manage, I
proposed my current company to do code reviews. As the tool, we choose
Phabricator. At first I guess I'll choose Gitlab, or even Atlasian, but
Phabricator seems worth to be tried.

Seriously, you can get general information about phabricator by just
google it. Here I am just sharing my experiences.

<!--more-->

[]()

### What Phabricator can do for you ?

Phabricator is complete collection of software intended to aids software
development. Some feature are already complete, some in prototype phase.
For now, Phabricator can do:

1.  Repository Hosting Management
2.  Code Review
3.  Project and Task Management.
4.  Wiki
5.  Kind of chat room called "Conpherence"
6.  and many more

[]()

### Why Phabricator ?

We choose phabricator becouse of some reasons :

1.  It's LAMP application, which is also our daily environment.
2.  Free and Open
3.  Why Not ?

[]()

### Install

You can follow the instruction
https://secure.phabricator.com/book/phabricator/article/installation\_guide/.
First repo pull via http, I got error about `git-http-backend`. If you
do too, you can do the following:

    cd  /path/tp/phabricator/support/bin
    sudo ln -sv /usr/lib/git-core/git-http-backend

[]()

### Herald

Herald is phabricator application you can use to control data in
phabricator, for example, In my company I need to restrict some push
when no accepted revision exists, then I use herald to control it. I
make the herald rule as following:

    When all of these conditions are met:
    Accepted Differential revision does not exist
    Pusher is not any of <username>

    Take these actions every time this rule matches:
    Block change with message Review is required for all changes.

[]()

### Differential Test Plan

By default, when creating a revision thru `arc diff` , you will be
prompted to fill test plan. If you don't need it, you can turn it off
by:

    phabricator/$ ./bin/config set differential.require-test-plan-field false

and edit `differential.fields` to the following:

     "differential:test-plan": {
        "key": "differential:test-plan",
        "disabled": true
    }

You can go to **Config** application by clicking Config on sidebar menu.
