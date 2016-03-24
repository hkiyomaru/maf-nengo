#MAF Generator

MAF is an abbreviation for Master Algorithm Framework,

and this has a big role to build a brain-inspired cognitive architecture.

I programed some scripts.

They can build MAF database, and create a rough [Nengo](http://www.nengo.ca/) scripts.

##Getting started

Clone this repository.

```
$ git clone https://github.com/kiyomaro927/maf_nengo.git
```

Then, ```cd seeds```.

You'll see three CSV files.

* mojules.csv
* connections.csv
* cortexes.csv

They become seeds to build MAF database.

Actually, however, they are dummy data.

So, you must collect data by every means.

###mojules.csv

![mojules.csv](https://raw.github.com/wiki/kiyomaro927/maf_nengo/images/mojules.PNG)

* name : area's name
* major_region : it's major region's name

###connections.csv

![mojules.csv](https://raw.github.com/wiki/kiyomaro927/maf_nengo/images/connections.PNG)

* source_name : area's name
* destination_name : area's name
* type : FF/FB/unk (FeedForward, FeedBack, Unknown)

###cortexes.csv

![mojules.csv](https://raw.github.com/wiki/kiyomaro927/maf_nengo/images/cortexes.PNG)

* source_major_region : major region's name
* destination_major_region : major region's name
* type : FF/FB/unk
* source_laminal : area's name/C1/C2_3/C4/C5/C6/unk
* destination_laminal : area's name/C1/C2_3/C4/C5/C6/unk

##Build MAF database.

![build_database](https://raw.github.com/wiki/kiyomaro927/maf_nengo/images/db_build.PNG)

I prepared a shell script.

You can create the database and insert the all seed data by executing this command.

```
$ ./db.sh
```

##Create Nengo Script

![create_nengo_script](https://raw.github.com/wiki/kiyomaro927/maf_nengo/images/create_nengo_script.PNG)

After building the database,

all you have to do is type this command and press the return key.

```
$ python generate_nengo_model.py
```

##Nengo GUI

Then, check the created script.

Let's use nengo-gui.

```
$ nengo_gui maf.py
```

I know you will witness a terrible graph.

I prepared a little seed data to check the program operation.

Of cource, data is dummy.

This is sample.

![sample](https://raw.github.com/wiki/kiyomaro927/maf_nengo/images/nengo_gui.PNG)


