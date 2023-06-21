# License year updater

This script will parse license file(s) passed to it and update the years.

Example 1 - updating the end year:
```diff
-Copyright (c) 1998-2019 John Doe <jdoe@example.com>
+Copyright (c) 1998-2020 John Doe <jdoe@example.com>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
```

Example 2 - adding the end year:
```diff
-Copyright (c) 2019 John Doe <jdoe@example.com>
+Copyright (c) 2019-2020 John Doe <jdoe@example.com>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
```

Example 3 - multiple copyright holders:
```diff
-Copyright (c) 2015-2018 John Doe <jdoe@example.com>
-Copyright (c) 2017-2018 Philip J. Fry <pfry@example.com>
+Copyright (c) 2015-2020 John Doe <jdoe@example.com>
+Copyright (c) 2017-2020 Philip J. Fry <pfry@example.com>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
```

## Usage

```bash
$ python3 update.py --help
usage: update.py [OPTION]

Updates license file(s) to the current year.

options:
  -h,--help             show this help message and exit
  -f,--files FILES      multiline string of file paths
  -e,--exclude EXCLUDE  multiline string of words in author to exclude
```

#### Files

To pass it multiple files use `update.py -f 'file1.txt\nfile2.txt'`.

#### Exclude option

The `exclude` option lets you select not to update the year for words matching certain authors.

Given this example:
```
Copyright (c) 2015-2018 John Doe <jdoe@example.com>
Copyright (c) 2017-2018 Philip J. Fry <pfry@example.com>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
```

You want to update the year for all authors, except "John Doe".
Invoke the script excluding parts of the author: `update.py -f license.txt -e 'jdoe@example.com'`

The result would be:
```diff
Copyright (c) 2015-2018 John Doe <jdoe@example.com>
-Copyright (c) 2017-2018 Philip J. Fry <pfry@example.com>
+Copyright (c) 2017-2023 Philip J. Fry <pfry@example.com>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
```

You can be as verbose as you want, targeting domains (`-e 'example.com'`) or names (`-e john`).
To pass multiple filters separate them by newline: `-e 'john\nalice'`

## GitHub Action

This is an example workflow that will do the following:
- check out the project
- use this script as an action, passing it a license file
- create a pull request

This will occur on January 1st every year at 03:00.

```yaml
name: Update copyright year in license file

on:
  schedule:
    - cron: '0 3 1 1 *'

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Clone project
        uses: actions/checkout@v3

      - name: Update license year
        uses: p3lim/license-year-updater@v2
        with:
          files: |
            license1.txt
            license2.txt

      - name: Create pull request
        uses: peter-evans/create-pull-request@v5
        with:
          title: Update license
          commit-message: Update license
          branch: update-license
          delete-branch: true
```

If you don't want to wait for Jan 1st every year and would like to run this action immediately, you can manually trigger it with `workflow_dispatch` in your workflow:

```yaml
on:
  workflow_dispatch:
```

With this you can trigger the workflow manually from the workflow page, see [this blog post](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/) for more information.
