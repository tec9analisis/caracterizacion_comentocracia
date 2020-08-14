#!/usr/bin/env wolframscript
(* ::Package:: *)

tw = ServiceConnect["Twitter"]


followed={"AristeguiOnline", "Forbes_Mexico", "LaJornada"};


GetHyperlinks[data_]:=Select[#,StringMatchQ["http"~~__]]&/@TextWords/@data[All,"Text"]


Do[
	twlist = tw["TweetList", "Username"->follow, "Elements"->"FullData", MaxItems->400];
	todaystweets = Select[twlist, DateWithinQ[Yesterday, #["Date"]]&];
	Export["C:\\Users\\User\\Documents\\Tweets\\"<>follow<>"\\"<>DateString[Yesterday, "ISODate"]<>".csv",
	Dataset@AssociationThread[
		Normal@todaystweets[All, "ID"],
		Normal@GetHyperlinks@todaystweets]
	];
	
,{follow, followed}];
