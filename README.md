Loading_Bar
=========
 Package contatining custom python loading bar object

To get started:

	from LoadingBar import LoadingBar

Initialize loading bar object with number of epochs:
	
	LB=LoadingBar(n, barLength=40, give_ETA=True)

* n is the number of epochs
* barLength is the length in characters of the loading bar
* give_eta is a flag indicating whether the an estimate of completion should be given

Execute self.load() upon every epoch, and self.end() after the final epoch

Eg.

	#initialize loading bar for a for loop with 40 loops of length 20 that gives eta
	LB=LoadingBar(40, barLength=20)
	for i in range(40):
		LB.load()
	LB.end()

After 1 epoch, the output is this:

	1/40 [--------------------] 2.50% ETA: 0:03:12

After 20 epochs:

	20/40 [++++++++++----------] 50.00% ETA: 0:01:41

After 25 epochs:

	25/40 [++++++++++++--------] 62.50% ETA: 0:01:13

After the last epoch and final call of LB.load():

	39/40 [+++++++++++++++++++-] 97.50% ETA: 0:00:04

And after the call of LB.end():

	40/40 [++++++++++++++++++++] 100.00% ETA: 0:00:00



A bar of barlength=40 with the give_ETA flag false would look somthing like this:

	8/40 [++++++++--------------------------------] 20.00%

Use self.reset() to reset the epoch count to 0, and self.setIter to set the epoch count manually

Created by [Josh Lassman](http://fishpoopsoup.com)
