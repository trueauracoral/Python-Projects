/////////////////////////////////////////////////////////////////////
//                                                                   /
// DESCRIPTION:                                                      /
// This is a file for changing odysee links into a chosen link in the/
// variables.                                                        /
//                                                                   /
// LISCENSE INFO (A dedicated liscense file is in the repo.):        /
//      ALL THE CODE IN THIS REPOSITORY INCLUDING THIS FILE IS       /
// (C) TrueAuraCoral and Other Contributors 2021.                    /
// YOU CAN USE THIS FILE AND ANY OTHER FILE IN THIS REPOSITORY UNDER /
// THE TERMS OF GNU GENERAL PUBLIC LICENSE VERSION 3 OR ANY LATER    /
// VERSION. TO FIND THE FULL TEXT OF THE LICENSE GO TO THE GNU.ORG   /
// WEBSITE AT ( https://www.gnu.org/licenses/gpl-3.0.html ).         /
/////////////////////////////////////////////////////////////////////

// ==UserScript==
// @name           odysee to librarian
// @namespace      Zera's userscripts
// @match          http://odysee.com/*
// @match          https://odysee.com/*
// @match          http://www.odysee.com/*
// @match          https://www.odysee.com/*
// @run-at         document-start
// ==/UserScript==

url = location.href
url = url.replace(/\bwww\.\b/, "")
url = url.replace("odysee.com","librarian.bcow.xyz")
location.href = url