const {app, BrowserWindow} = require("electron");
const path = require("path");
const url = require("url");

//init win
let win;

function createWindow(){
   win = new BrowserWindow({fullscreen:true});

     // and load the index.html of the app.
    win.loadURL(url.format({
        pathname: path.join(__dirname, "index.html"),
        protocol: "file:",
        slashes:true

    }));

   //closed event
   win.on("closed", () =>{
       win = null;
   });

   win.webContents.openDevTools();
}

//run createWin
app.on("ready", createWindow);

//close when all windows are close
app.on("window-all-closed", app.quit);