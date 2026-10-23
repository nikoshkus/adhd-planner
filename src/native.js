// Підключає нативні плагіни Capacitor і віддає їх застосунку через window.NP.
import { Capacitor } from '@capacitor/core';
import { LocalNotifications } from '@capacitor/local-notifications';
import { CapacitorCalendar } from '@ebarooni/capacitor-calendar';
import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';

window.NP = {
  native: Capacitor.isNativePlatform(),
  LocalNotifications,
  CapacitorCalendar,
  Filesystem,
  Directory,
  Encoding,
  Share,
};
