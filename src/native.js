// Підключає нативні плагіни Capacitor і віддає їх застосунку через window.NP.
import { Capacitor } from '@capacitor/core';
import { App } from '@capacitor/app';
import { LocalNotifications } from '@capacitor/local-notifications';
import { CapacitorCalendar } from '@ebarooni/capacitor-calendar';
import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';
import { Preferences } from '@capacitor/preferences';
import { Share } from '@capacitor/share';

window.NP = {
  native: Capacitor.isNativePlatform(),
  App,
  LocalNotifications,
  CapacitorCalendar,
  Filesystem,
  Directory,
  Encoding,
  Preferences,
  Share,
};
