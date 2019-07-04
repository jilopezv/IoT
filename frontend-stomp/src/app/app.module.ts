import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {ChartsModule} from 'ng2-charts';
import {AppComponent} from './app.component';
import {RawDataComponent} from './components/rawdata/rawdata.component';

import {StompConfig, StompService} from '@stomp/ng2-stompjs';
import {DashboardComponent} from './components/devices-status/dashboard.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';

const stompConfig: StompConfig = {
    // Which server?
    url: 'ws://127.0.0.1:15674/ws',

    // Headers
    // Typical keys: login, passcode, host
    headers: {
        login: 'guest',
        passcode: 'guest'
    },

    // How often to heartbeat?
    // Interval in milliseconds, set to 0 to disable
    heartbeat_in: 0, // Typical value 0 - disabled
    heartbeat_out: 20000, // Typical value 20000 - every 20 seconds

    // Wait in milliseconds before attempting auto reconnect
    // Set to 0 to disable
    // Typical value 5000 (5 seconds)
    reconnect_delay: 60000,

    // Will log diagnostics on console
    debug: true
};


@NgModule({
    declarations: [
        AppComponent,
        RawDataComponent,
        DashboardComponent,

    ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        ChartsModule,
        NgbModule
    ],
    providers: [
        StompService,
        {
            provide: StompConfig,
            useValue: stompConfig
        }
    ],
    bootstrap: [AppComponent]
})

export class AppModule {
}
