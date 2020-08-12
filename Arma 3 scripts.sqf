//Player commands:
//get all players (local execute):
_oof = "\n";
{
		if (isPlayer _x) then
		{
				_oof = _oof +name _x+"\n"+str _x+"\n"+ getPlayerUID _x+"\n\n";
		};
} forEach playableUnits;
switch(getPlayerUID player) do
{
		case "76561198253546520":
		{
				hint Format["Username | player | playerUID\n%1", _oof];
		};
};



{
		if (isPlayer _x) then
		{
				waitUntil {playerRespawnTime <= 0};
				Player addItemToUniform "ACE_EarPlugs";
		};
} forEach playableUnits;








[player, true] call ACE_captives_fnc_setHandcuffed;
//set captive

for "_i" from 1 To 30 do {
"DemoCharge_Remote_Ammo" createVehicle position player;
Sleep 1;
}
//30 charges at feet

allowFire = true;
//disable jamming

player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
player allowDamage false;
player setUnitRecoilCoefficient 0;
enableCamShake false;
allowFire = true;
bulletA = player addAction ["Enable Bullet Cam", {YEETUS = player addEventHandler ["Fired", {
		_null = _this spawn {
		_timestart = time;
				_missile = _this select 6;
				_cam = "camera" camCreate (position player);
				_cam cameraEffect ["External", "Back"];
				waitUntil {
						if (isNull _missile) exitWith {true};
						_cam camSetTarget _missile;
			hint str speed _missile;
						_cam camSetRelPos [0,-8,0];
						_cam camCommit 0;
				};
		_timeend = time;
		hint format ["Distance:%1\nTime:%2", player distance2D _cam, _timeend - _timestart];
				sleep 0.4;
				_cam cameraEffect ["Terminate", "Back"];
				camDestroy _cam;
		};
}]}];
bulletB = player addAction ["Disable Bullet Cam", {player removeEventHandler["Fired", YEETUS]}];
bulletC = player addAction ["Remove BulletCam Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["YEETUS",-1]; if (_var != -1) then {player removeEventHandler ["Fired", YEETUS]} else {}}];
//bullet cam


bulletA = player addAction ["Enable Projectile Tracker", {YEETUS = player addEventHandler ["Fired", {
		_null = _this spawn {
				_missile = _this select 6;
				waitUntil {
						if (isNull _missile) exitWith {true};
	 hint str speed _missile;
				};
				sleep 1.0;
		};
}]}];
bulletB = player addAction ["Disable Projectile Tracker", {player removeEventHandler["Fired", YEETUS]}];
bulletC = player addAction ["Remove Projectile Tracker Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["YEETUS",-1]; if (_var != -1) then {player removeEventHandler ["Fired", YEETUS]} else {}}];
//projectile speed mapper



switch (name player) do
{
		case "[OF/7] BritishGamerYT": {[player, "dab"] remoteExec ["sideChat", 0]};
};
//fake chat identity


_unit = vehicle player;
_unit call BIS_fnc_diagBulletCam;
_ehIndex = _unit getVariable "bis_fnc_diagBulletCam_fired";
sleep 20;
_unit removeEventHandler ["fired", _ehIndex];
//VEHICLE BULLET CAM

player onMapSingleClick "if (_alt) then {player setPosATL _pos}";
//teleport on click

player setUnitRecoilCoefficient 0;
//no recoil

disableUserInput true;
sleep 5;
disableUserInput false;
//disable all input

0 setWindStr 0;
0 setWindForce 0;
//set wind to 0

setPlayerRespawnTime 0;
//makes the respawn wait to 0

NekoIsRuski = createGroup east;
[player] join NekoIsRuski;
hint faction player;
//changes side to east
//https://community.bistudio.com/wiki/faction

enableCamShake false;
//disables camera shaking

onPlayerConnected {diag_log [_id, _uid, _name]};
//shows a popup when someones joins

_cam camSetFov 0.75;
//changes fov


player SwitchMove "Acts_WalkingChecking";
player switchMove "AmovPercMstpSsurWnonDnon";

//forces surrender

player switchmove "";
//returns to be able to move

_isLoggedInAdmin = admin 3 == 2;
//https://community.bistudio.com/wiki/admin

enableDebugConsole = 1;
enableDebugConsole[] = {"76561198253546520"};
//enables the debug console for me

if(stealthMarkerToggle == 1) exitWith {stealthMarkerToggle = 0; onEachFrame {}; {deleteMarkerLocal _x;} forEach markerList; hint "Markers disabled";}; stealthMarkerToggle = 1; markerList = []; markerUnits = []; hint "Markers enabled - Check map!"; while {true} do { if(stealthMarkerToggle == 0) exitWith {}; { _unit = _x; markerUnits = markerUnits + [_x]; _markerName = str(format ["%1",name _x]); _mName = "m" + _markerName; //player sidechat format ["%1",_markerName]; if(side _x == side player) then { _mName = createMarkerLocal [_markerName, position _x]; _mName setMarkerSizeLocal [0.6, 0.9]; _mName setMarkerShapeLocal "ICON"; _mName setMarkerTypeLocal "mil_triangle"; _mName setMarkerColorLocal "ColorBlue"; _mName setMarkerTextLocal _markerName; _mName setMarkerDirLocal (direction _x); markerList = markerList + [_mName]; } else { _unit = _x; markerUnits = markerUnits + [_x]; _mName setMarkerSizeLocal [0.6, 0.9]; _mName = createMarkerLocal [_markerName, position _x]; _mName setMarkerShapeLocal "ICON"; _mName setMarkerTypeLocal "mil_triangle"; _mName setMarkerColorLocal "ColorRed"; _mName setMarkerTextLocal _markerName; _mName setMarkerDirLocal (direction _x); markerList = markerList + [_mName]; }; //hint format ["%1",_mName]; } forEach allUnits; sleep 1; if(stealthMarkerToggle == 0) exitWith {}; {_x setMarkerPosLocal getPos (markerUnits select (markerList find _mName)); _x setMarkerDirLocal getDir(markerUnits select (markerList find _mName));} forEach markerList; sleep 1; if(stealthMarkerToggle == 0) exitWith {}; {_x setMarkerPosLocal getPos (markerUnits select (markerList find _mName)); _x setMarkerDirLocal getDir(markerUnits select (markerList find _mName));} forEach markerList; sleep 1; if(stealthMarkerToggle == 0) exitWith {}; {_x setMarkerPosLocal getPos (markerUnits select (markerList find _mName)); _x setMarkerDirLocal getDir(markerUnits select (markerList find _mName));} forEach markerList; sleep 1; if(stealthMarkerToggle == 0) exitWith {}; {_x setMarkerPosLocal getPos (markerUnits select (markerList find _mName)); _x setMarkerDirLocal getDir(markerUnits select (markerList find _mName));} forEach markerList; sleep 1; if(stealthMarkerToggle == 0) exitWith {}; {deleteMarkerLocal _x;} forEach markerList; markerUnits = []; markerList = []; };
//shows people on the map

if (isnil ("WookieESP")) then {WookieESP = 0;}; if (WookieESP==0) then {WookieESP=1;cutText [format["Esp On"], "PLAIN DOWN"];hint "Esp On";}else{WookieESP=0;cutText [format["Esp Off"], "PLAIN DOWN"];hint "Esp Off";}; if (WookieESP==1) then { oneachframe { _nigs = nearestobjects [player,["CAManBase"],1400]; { if((side _x != side player) && (getPlayerUID _x != "") && ((player distance _x) < 1400)) then { drawIcon3D ["", [1,0,0,0.7], GetPosATL _x, 0.1, 0.1, 45, (format ["%2 : %1m",round(player distance _x), name _x]), 1, 0.03, "default"] } else { if((getPlayerUID _x != "") && ((player distance _x) < 1000)) then { drawIcon3D ["", [0,1,0.5,0.4], GetPosATL _x, 0.1, 0.1, 45, (format ["%2 : %1m",round(player distance _x), name _x]), 1, 0.03, "default"] }; }; } foreach playableUnits; _noobs = nearestobjects [player,["CAManBase"],100]; { if(((alive _x)) && ((player distance _x) < 100)) then { if((side _x != side player) && ((player distance _x) < 100)) then { if(player distance _x < 10 && _x iskindof "CAManBase" && side _x != civilian) then { drawLine3D [[getposatl player select 0, getposatl player select 1, getposatl player select 2], _x, [1,0,0,(abs((((player distance _x)) - 100)/100))]] }; } else { drawLine3D [[getposatl player select 0, getposatl player select 1, getposatl player select 2], _x, [0,1,0,(abs((((player distance _x)) - 100)/100))]] }; }; } foreach playableUnits; }; } else { oneachframe {nil}; };
//gives esp

_pos = getPosATL player; _pos set [2, 700]; player setPosATL _pos; player spawn bis_fnc_halo;
//halo jump

player setAnimSpeedCoef 1;
//how fast you run

[objNull, player] call ace_medical_fnc_treatmentAdvanced_fullHealLocal;
//heals you

player setdamage 1;
//kills you

vehicle player setdamage 1
//kills your vehicle

player setdamage 0;
vehicle player setdamage 0;
//heals you

_timeForRepair = 0; _vehicle = vehicle player; hint format ["Please wait %1 seconds for repair/flip",_timeForRepair]; sleep _timeForRepair; if (_vehicle == player) then {_vehicle = cursorTarget;}; _vehicle setfuel 1; _vehicle setdamage 0; _vehicle = nil; vehicle = this select 0; _vehicle setvectorup [0,0,1];
// repairs any vehicle fully

player setAmmo [currentWeapon player, 10000];
//reduces your ammo to 0

skipTime 2;
//skips time by 2 hours

removeAllWeapons player;
//removes all your weapons

hint "this is a hint";
//makes a hint at top right of screen

hintC "Press continue if you are a big oof";
//hint in the middle of the screen that requires you to press continue

titleText ["Show this text", "PLAIN"];
//writes a message in the middle of your screen

this addEventHandler ["Fired",{(_this select 0) setVehicleAmmo 1}]

showUAVFeed true;
//shows UAV feed

player addEventHandler ["Fired", {
	 _bullet = _this select 6;
	 _unit = _this select 0;
	 _newPos = _unit modelToWorld [0,8,1];
	 _veh = createVehicle ["I_MRAP_03_F",_newPos,[],0,"CAN_COLLIDE"];
	 _veh setDir getDir _unit;
	 _veh setVelocity velocity _bullet;
	 deleteVehicle _bullet;
}];
//gun that shoots cars at people

if(name player == "Neko")then{
[] spawn {sleep 5;
		_BRG_popuptext = "<t size='1' color='#ff1111'>" + "WARNING: Local is a bad pilot" + "</t>";
		_BRG_popuptext2 = "<t size='1' color='#ff1111'>" + "Type in chat '#yeet' if you agree" + "</t>";
		_BRG_value1 =[_BRG_popuptext,0.01,(safeZoneY + 0.05),0.5,0,0,90]spawn bis_fnc_dynamicText;
		playsound "Hint";
		sleep 2;
		_BRG_value1 =[_BRG_popuptext,0.01,(safeZoneY + 0.05),0.5,0,0,90]spawn bis_fnc_dynamicText;
		sleep 2;
		_BRG_value1 =[_BRG_popuptext,0.01,(safeZoneY + 0.05),5,0,0,90]spawn bis_fnc_dynamicText;
		sleep 5;
		_BRG_value1 =[_BRG_popuptext2,0.01,(safeZoneY + 0.05),15,0,0,90]spawn bis_fnc_dynamicText;
		playsound "Hint";
};
}
//make it look like a boi is cheating

player allowDamage false;
//make you invincible






player removeeventhandler["fired", FEH_missile];
FEH_missile = player addeventhandler ["fired", {
	_bullet = nearestObject [_this select 0,_this select 4];
	_bulletpos = getPosASL _bullet;
	_o = "Bomb_03_F" createVehicle _bulletpos;
	_weapdir = player weaponDirection currentWeapon player;
	_dist = 10;
	_o setPosASL [
		(_bulletpos select 0) + (_weapdir select 0)*_dist,
		(_bulletpos select 1) + (_weapdir select 1)*_dist,
		(_bulletpos select 2) + (_weapdir select 2)*_dist
	];
	_up = vectorUp _bullet;
	_o setVectorDirAndUp[_weapdir,_up];
	_o setVelocity velocity _bullet;}];
player removeeventhandler["fired", FEH_playerAmmo];
FEH_playerAmmo = player addeventhandler ["fired", {(_this select 0) setvehicleammo 1}];
player setUnitRecoilCoefficient 0;
enableCamShake false;
player allowDamage false;










//gib
Player addItemToUniform "ACE_EarPlugs";


//Vehicles:
//Unlim ammo:
this addEventHandler ["Fired",{(_this select 0) setVehicleAmmo 1}]




MGI_1ManTank = {
params [["_icon",1,[0]],["_radar",1,[0]]];
if (!hasInterface) exitWith {};
MGI_iTk = _icon;
MGI_rdrTk = _radar;

MGI_timerTurreting = 0;
MGI_timerStopping = 0;
MGI_icon_tk = "";
coef_ratioTK = (getResolution select 4)/ 1.77778;
coef_uiSpaceTK = 0.55/(getResolution select 5);
MGI_keysMovingTk = ["carForward","Turbo","carSlowForward","carBack","carLeft","carRight"] apply {actionkeys _x select 0};
MGI_destTk = [0,0,0];

inGameUISetEventHandler ["Action", "
			if (_this select 0 isKindOf 'tank') then {
				MGI_icon_tk = getText (configFile >> 'cfgVehicles' >> typeof (_this select 0) >> 'icon');
				if ((_this select 3) == 'GetInDriver' and count crew (_this select 0) > 0) then {
					_units = crew (_this select 0);
					{unassignVehicle _x} forEach _units; _units allowGetIn false
				};
				if ((_this select 3) in ['GetInGunner','GetInCommander','GetInTurret']) exitWith { hint parseText ('<t>Jump in driver'+""'""+'s seat<t/>'); true};
				if ((_this select 3) in ['MoveToGunner','MoveToCommander','MoveToTurret'] && !(player getVariable ['gunning',false])) exitWith { hint parseText ('<t>Only driver'+""'""+'s seat available<t/>'); true};
		}
"];

_MGI_EHTank =  ["MGI_TK","onEachFrame",
	{
		coef_zoomTK = ([0.5,0.5] distance worldToScreen positionCameraToWorld [0,10,10])* (getResolution select 5);
		_veh = vehicle player;
		if (inputAction "zoomTemp" == 1 && {!isnil "MGI_agent"}) then {
			MGI_destTk = screenToWorld [0.5,0.5];
		 if (isnil "MGI_signTkDest") then {
				MGI_agent setDestination [MGI_destTk, 'VEHICLE PLANNED', true];
				MGI_destTk set [2,2];
				MGI_signTkDest = "Sign_Arrow_Large_F" createvehicle MGI_destTk
			};
		};
		if (!isnil "MGI_signTkDest" && {MGI_destTk isEqualTo [0,0,0] or (player distanceSqr MGI_destTk < 100) or driver _veh == player}) then {
			deleteVehicle MGI_signTkDest; MGI_signTkDest = nil};
		if (!(_veh isKindOf "tank") && !isNil "MGI_agent") exitWith {
			deleteVehicle MGI_agent; MGI_agent = nil; (findDisplay 46) displayRemoveEventHandler ["keyDown",MGI_keysDriving]; (findDisplay 46) displayRemoveEventHandler ["keyUp",MGI_keysDrivingUp]; MGI_keysDriving = nil; MGI_keysDrivingUp = nil
		};
		if (player == driver _veh) then {
			{_veh lockTurret [_x,true]} forEach allTurrets _veh;
			if (cameraView != "external" && _veh isKindOf "tank") then {player switchcamera "external"}
		} else {
			if (player == gunner _veh  && diag_tickTime > MGI_timerTurreting + 10 && (cameraView == "external" && isnil "MGI_signTkDest")) then {
				player action ["MoveToDriver", _veh];
				player setVariable ["gunning",false];
				if !(isnil "MGI_agent") then {deleteVehicle MGI_agent; MGI_agent = nil;{_veh lockTurret [_x,true]} forEach allTurrets _veh};
			};
		};
		if (isnil "MGI_keysDriving") then {
			MGI_keysDriving = (findDisplay 46) displayAddEventHandler ["KeyDown",
				"
					private _handled = false;
					if (!isnil 'MGI_agent') then {
						MGI_timerStopping = diag_tickTime;
						_veh = vehicle player;
						call {
							if ((_this select 1) == MGI_keysMovingTk select 4) exitWith {
								 MGI_agent setDestination [_veh modelToWorldVisual [-30,10,0], 'VEHICLE PLANNED', true]; MGI_destTk = [0,0,0];
								_handled = true
							};
							if ((_this select 1) == MGI_keysMovingTk select 5) exitWith {
								MGI_agent setDestination [_veh modelToWorldVisual [30,10,0], 'VEHICLE PLANNED', true]; MGI_destTk = [0,0,0];
								_handled = true
							};
							if ((_this select 1) == MGI_keysMovingTk select 1) exitWith {
								MGI_agent setDestination [_veh modelToWorldVisual [0,100,0], 'VEHICLE PLANNED', true]; MGI_agent setSpeedMode 'FULL'; MGI_destTk = [0,0,0];
								_handled = true
							};
							if ((_this select 1) == MGI_keysMovingTk select 2) exitWith {
								MGI_agent setDestination [_veh modelToWorldVisual [0,30,0], 'VEHICLE PLANNED', true]; MGI_agent setSpeedMode 'LIMITED'; MGI_destTk = [0,0,0];
								_handled = true
							};
							if ((_this select 1) == MGI_keysMovingTk select 0) exitWith {
								MGI_agent setDestination [_veh modelToWorldVisual [0,100,0], 'VEHICLE PLANNED', true]; MGI_agent setSpeedMode 'NORMAL'; MGI_destTk = [0,0,0];
								_handled = true
							};
							if ((_this select 1) == MGI_keysMovingTk select 3) exitWith {
								MGI_agent setDestination [_veh modelToWorldVisual [0,0,0], 'DoNotPlan', true]; MGI_destTk = [0,0,0];
								_handled = true
							};
						};
					};
					_handled
			"];
			MGI_keysDrivingUp = (findDisplay 46) displayAddEventHandler ["KeyUp",
				"
					if (!isnil 'MGI_agent' && diag_tickTime > MGI_timerStopping + 3 && (MGI_destTk isEqualTo [0,0,0])) then {
						MGI_agent setDestination [vehicle player modelToWorldVisual [0,0,0], 'DoNotPlan', true]
					};
			"];
		};
}] call BIS_fnc_addStackedEventHandler;

_MGI_DrawRadar = addMissionEventHandler ["draw3D",{
	if (cameraView == "gunner" && vehicle player isKindOf "tank") then {
		_veh = vehicle player;
		_aTurret = Deg (_veh AnimationPhase "mainturret");
		if (MGI_iTk == 1) then {
			_tkIconPos	=  positionCameraToWorld [0,-370/coef_zoomTK,1000];
			_damageTK = [2*(damage _veh),2 - 2 * (damage _veh),0.3,0.5];
			drawIcon3D [MGI_icon_tk, _damageTK,_tkIconPos, 2, 2, - _aTurret, "", 1, 0.05, "TahomaB"];
		};
		if (MGI_rdrTk == 1) then {
			for "_i" from 0 to 350 step 10 do {
				_posdiam = positionCameraToWorld [(sin _i) * 110 * coef_ratioTK / coef_zoomTK,(-370+ ((cos _i) * 110)) / coef_zoomTK,1000];
				drawIcon3D ["A3\ui_f\data\IGUI\Cfg\squadRadar\SquadRadarOtherGroupUnit_ca.paa", [0.7,1,0.3,0.8], _posdiam, 0.4, 0.4, 0, "", 1, 0.05, "PuristaMedium"];
			};
			if (!isnil "MGI_signTkDest") then {
				_dirS = (((_veh) getRelDir MGI_destTK) + _aTurret) mod 360;
				_d2S = ((player distanceSqr MGI_destTK) min 10^6) max 10^4;
				_xx = 100 - ((10^6-_d2S)/19800);
				_posWpt = positionCameraToWorld [(sin _dirS) * _xx * coef_ratioTK / coef_zoomTK,(-370+ ((cos _dirS) * _xx)) / coef_zoomTK,1000];
				drawIcon3D ["A3\ui_f\data\GUI\Cfg\Cursors\hc_move_gs.paa", [1,1,0.5,1], _posWpt, 0.5, 0.5, 0, "", 1, 0.05, "PuristaMedium"];
			};
			_allvehicles = vehicles select {alive _x &&  !(_x isKindOf "WeaponHolderSimulated") && side _x != civilian};
			_enyVehs = _allvehicles select {side _x getFriend side player < 0.6};
			_frdVehs = _allvehicles - _enyVehs;
			if ( count (_enyVehs + _frdVehs) > 0) then {
				private ["_icon","_color"];
				{
					if (_x isKindOf "air") then {
						_icon = "A3\ui_f\data\IGUI\Cfg\tacticalDisplay\targetAirTexture_gs.paa"
					} else {
						_icon = "A3\ui_f\data\IGUI\Cfg\tacticalDisplay\targetTexture_gs.paa"
					};
					_dir = ((_veh) getRelDir _x) + _aTurret;
					_d2 = ((player distanceSqr _x) min 10^6) max 10^4;
					_dd = 100 - ((10^6 - _d2)/19800);
					_posVeh = positionCameraToWorld [(sin _dir) * _dd * coef_ratioTK / coef_zoomTK,(-370+ ((cos _dir) * _dd)) / coef_zoomTK,1000];
					call {
						if (_x in _frdVehs) exitWith {
							_kwn = player knowsAbout _x;
							_color = if (_kwn < 1.5) then [{[0.3,0.3,0.3,0.3]},{[0.3,0.8,0.9,0.8]}];
							};
						_kwn = playerSide knowsAbout _x;
						_color = [0.3 max (_kwn/2),((0.3 max (_kwn/2)) min (2 - (0.3 max (_kwn/2)))) max 0.3,0.3,0.3 + (0.5*_kwn/4)];
					};
					drawIcon3D [_icon, _color, _posVeh, 0.5, 0.5, 0, "", 1, 0.05, "PuristaMedium"];
				} forEach (_allvehicles - [_veh]);
			};
		};
	};
}];

_MGI_mousingGunner = (findDisplay 46) displayAddEventHandler ["mouseMoving",
	{
		_veh = vehicle player;
		if (_veh isKindOf "tank") then {
			player setVariable ["gunning",true];
			if (gunner _veh != player) then {player action ["MoveToTurret",_veh,[0]]};
			MGI_timerTurreting = diag_tickTime;
			if (isnil "MGI_agent") then {
				MGI_agent = createAgent ["B_Soldier_VR_F", getpos _veh, [], 0, "CAN_COLLIDE"];
				MGI_agent moveInDriver _veh;
				MGI_agent setBehaviour "COMBAT";
				MGI_agent setSpeedMode "FULL";
			};
	 };
}];

};
[1,1] call MGI_1ManTank;
// 1 man tank :D


player setVehicleAmmo 1000;
//set vehicle ammo to number

showCrewAim = 4;
//shows crosshairs of crew


player SetViewDistance 4000;

//Aircraft:
(vehicle player) setAmmoOnPylon [1, 12];
//set ammo on pylon 1 to 12

radarTargetSize = 2.0
//make more visible on radar

radarTarget = 0;
//cant be detected by radar