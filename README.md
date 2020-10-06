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

### Usage:

```bash
python3 update.py LICENSE.txt LICENSE_2.txt ...
```

You can specify as many files you want.
