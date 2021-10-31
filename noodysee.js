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