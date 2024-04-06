# RayCasting
Old project where I was testing Some russian video on Raycasting. 

<img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/8a2bde70-3ab0-4929-8b61-12c439003e32" alt="Cornstarch <3" width="55" height="59">

You kinda walk fast to watch out on that. I have been slowly making raycasters and stopping midway through on languages like C++ as I've been moving languages but may try with OpenGL next as I see C++ as my primary language. Still probably one of my nicer looking rasters amidst its spaghetti.

----------------------------------------------

<img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/7be2a422-4e4e-454c-a1d5-b4cd99c126e9" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/7be2a422-4e4e-454c-a1d5-b4cd99c126e9" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/7be2a422-4e4e-454c-a1d5-b4cd99c126e9" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/7be2a422-4e4e-454c-a1d5-b4cd99c126e9" alt="Cornstarch <3" width="55" height="49">


**The Breakdown:**

  This Program Works With Python And Its Pygame Library To Generate A Raycasting Engine Based Upon A 2D-Voxel-Map.

  The Program Starts By Initializing A Predefined Dimensioned Window. As Well As Our Window, We Will Start A GameClock. During Every MainLoop Tick, We Will Be Checking User Input For The Player's Movement. The Controls Will Be As Follows:

  &nbsp;- Press W: Move Forward.

  &nbsp;- Press S: Move Backward.

  &nbsp;- Press A: Move Left.

  &nbsp;- Press D: Move Right.

  &nbsp;- Press Right-Arrow: Turn Right.

  &nbsp;- Press Left-Arrow: Turn Left.
  

While Thats All We Can Do, And We Don't Really Have Collision With Walls In This Version, It's Still Quite Epic. A Lot Of This Project Relates To The More Backend Programming Of The Engine As Before This I only Used Static Textures Or Colors And Didn't Really Understand How We Could Make A 3D Space With a 2D Window.

The Ray Casting Algorithm Is Quite Trivial, Using A For-Loop To Count Through A Specified Amount Of Rays Defined In Our Settings.py Folder. This Is Done By Initially Getting The Polar-Coordinate Of Our Angle And Using Another Internal Nested-Loop In Order To Step Through Our World Space Until We Collide With A Wall Cell. When We Hit This Wall Cell We Will Calculate How For The Distance Is From Us And This Wall In Order To Draw Its Height On The Pygame Window. We Also Have A Shading Filter Added In Which Simply Increases The Shade Of Our Wall The Less Depth We Are To The Wall.

  While This Project Is Quite Dull In Features, It Was My First Actual PROJECT Where I Saw Myself Making A Multi-Object Program With More Intuitive Design And Modularity. While I Did Follow A Russian Video That I Couldn't Understand, At Least He Wrote His Code In English So It Really Challenged Me To Really Interpret What He Was Doing And Why. I Think This Really Benefitted Me In Development In My Later Projects As Coming Out Of This I Generally Saw How Windows ACTUALLY Work As Well As How We Draw A Window With Some Shape/Design. While Previously I Thought It Was Some Black Magic Voodoo WitchCraft, It Was Intruiging To See Actually How We Request Something Like A Window To Draw A Square Throughout These Given Coordinates With "R,G,B" Color Values.

  This Video Also Taught Me A Lot Of Good-Practice Decisions As Making Constants For Our Player Settings In Their Own File Was A Smart Move As It Allowed For A Non-Volatile Session Of Our Game. While This Isn't Really Necessary In Something Quite Hard-Coded As This Program In Its Current State, It Did At Least Get Me Comfortable With Some Concepts That I Do See Myself Using In Newer More Depthful Projects With Multi-Hierachical Relationships.

<img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/e1106c40-2320-4748-be36-c4aff6276c13" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/e1106c40-2320-4748-be36-c4aff6276c13" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/e1106c40-2320-4748-be36-c4aff6276c13" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/e1106c40-2320-4748-be36-c4aff6276c13" alt="Cornstarch <3" width="55" height="49">

----------------------------------------------

<img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/67926ce6-45d1-4f01-b045-9d6d7d523325" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/67926ce6-45d1-4f01-b045-9d6d7d523325" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/67926ce6-45d1-4f01-b045-9d6d7d523325" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/67926ce6-45d1-4f01-b045-9d6d7d523325" alt="Cornstarch <3" width="55" height="49">


**Features:**

![2024-01-0923-37-28-ezgif com-optimize](https://github.com/Kingerthanu/RayCasting/assets/76754592/5ff253b4-c88e-485d-aeb0-b7c9847e5ccf)
![3DRaster1](https://github.com/Kingerthanu/RayCasting/assets/76754592/039fcd9b-f984-4cd1-bae4-c0d142ebce6e)
![3DRaster2](https://github.com/Kingerthanu/RayCasting/assets/76754592/a5473ce6-a789-43f7-8d93-8b47a2ea7eea)
![3DRasterFar1](https://github.com/Kingerthanu/RayCasting/assets/76754592/a4d532b6-684f-4b5d-bc23-bd8e73870a97)
![3DRasterFar2](https://github.com/Kingerthanu/RayCasting/assets/76754592/1bd47685-3b16-4ad6-8b45-6ee3219bca45)



<img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/07761638-8ddc-418e-a6fc-60e70c7b0d8f" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/07761638-8ddc-418e-a6fc-60e70c7b0d8f" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/07761638-8ddc-418e-a6fc-60e70c7b0d8f" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/RayCasting/assets/76754592/07761638-8ddc-418e-a6fc-60e70c7b0d8f" alt="Cornstarch <3" width="55" height="49">
