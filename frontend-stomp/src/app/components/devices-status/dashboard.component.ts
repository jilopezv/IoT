import {Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {StompService, StompState} from '@stomp/ng2-stompjs';
import {map} from 'rxjs/operators';
import {BehaviorSubject, Observable, Subscription} from 'rxjs';
import {Message} from '@stomp/stompjs';
import {BaseChartDirective} from 'ng2-charts';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit, OnDestroy {
    @ViewChild(BaseChartDirective) tmpChart: BaseChartDirective;

    private subscription: Subscription;
    home_status;
    public watcher_status = new BehaviorSubject(false);
    public light_status = new BehaviorSubject(false);
    public alarm_color = new BehaviorSubject('#ebecf1');
    public tmpValues: Array<any> = [];

    public messages: Observable<Message>;
    // Subscription status
    public subscribed: boolean;
    public gradientStroke;
    public chartColor;
    public canvas: any;
    public ctx;
    public gradientFill;

    public gradientChartOptionsConfigurationWithNumbersAndGrid: any;

    public lineChartWithNumbersAndGridType;
    public lineChartWithNumbersAndGridData: Array<any>;
    public lineChartWithNumbersAndGridOptions: any;
    public lineChartWithNumbersAndGridLabels: Array<any>;
    public lineChartWithNumbersAndGridColors: Array<any>;

    // events
    public chartClicked(e: any): void {
        console.log(e);
    }

    public chartHovered(e: any): void {
        console.log(e);
    }

    public hexToRGB(hex, alpha) {
        const r = parseInt(hex.slice(1, 3), 16),
            g = parseInt(hex.slice(3, 5), 16),
            b = parseInt(hex.slice(5, 7), 16);

        if (alpha) {
            return 'rgba(' + r + ', ' + g + ', ' + b + ', ' + alpha + ')';
        } else {
            return 'rgb(' + r + ', ' + g + ', ' + b + ')';
        }
    }

    constructor(private _stompService: StompService, private modalService: NgbModal) {
    }

    open(content) {
        this.sendMessage('start_streaming');
        this.sleep(3000).then(() => {
            //do stuff
          })
        this.modalService.open(content, {size: 'lg'}).result.then((result) => {
            this.sendMessage('stop_streaming');
        }, (reason) => {
           this.sendMessage('stop_streaming');
        });
    }

  sleep = (milliseconds) => {
        return new Promise(resolve => setTimeout(resolve, milliseconds))
      }

    evaluarColor(state: number) {
        switch (state) {
            case StompState.CONNECTED:
                return 'green';
            case StompState.CLOSED:
                return 'gray';
            case StompState.TRYING:
                return 'orange';
            default:
                return 'red';

        }
    }

    ngOnInit() {
        this.subscribed = false;

        // Store local reference to Observable
        // for use with template ( | async )
        this.subscribe();

        console.log('Status init');
        this.home_status = this._stompService.state.pipe(
            map((state: number) => this.evaluarColor(state)));

        this.canvas = document.getElementById('temperatureChart');
        this.ctx = this.canvas.getContext('2d');


        this.chartColor = '#FFFFFF';
        this.gradientChartOptionsConfigurationWithNumbersAndGrid = {
            maintainAspectRatio: false,
            legend: {
                display: false
            },
            tooltips: {
                bodySpacing: 4,
                mode: 'nearest',
                intersect: 0,
                position: 'nearest',
                xPadding: 10,
                yPadding: 10,
                caretPadding: 10
            },
            responsive: true,
            scales: {
                yAxes: [{
                    gridLines: {
                        zeroLineColor: 'transparent',
                        drawBorder: false
                    }
                }],
                xAxes: [{
                    display: 0,
                    ticks: {
                        display: false
                    },
                    gridLines: {
                        zeroLineColor: 'transparent',
                        drawTicks: false,
                        display: false,
                        drawBorder: false
                    }
                }]
            },
            layout: {
                padding: {
                    left: 0,
                    right: 0,
                    top: 15,
                    bottom: 15
                }
            }
        };

        this.gradientStroke = this.ctx.createLinearGradient(500, 0, 100, 0);
        this.gradientStroke.addColorStop(0, '#cecb20');
        this.gradientStroke.addColorStop(1, this.chartColor);

        this.gradientFill = this.ctx.createLinearGradient(0, 170, 0, 50);
        this.gradientFill.addColorStop(0, 'rgba(128, 182, 244, 0)');
        this.gradientFill.addColorStop(1, this.hexToRGB('#ce1415', 0.4));

        this.lineChartWithNumbersAndGridData = [
            {
                label: 'Tmp Stats',
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 1,
                pointRadius: 4,
                fill: true,
                borderWidth: 2,
                data: this.tmpValues// [40, 500, 650, 700, 1200, 1250, 1300, 1900]
            }
        ];
        this.lineChartWithNumbersAndGridColors = [
            {
                borderColor: '#ce1415',
                pointBorderColor: '#FFF',
                pointBackgroundColor: '#ce1415',
                backgroundColor: this.gradientFill
            }
        ];
        this.lineChartWithNumbersAndGridLabels = [];// ['12pm,', '3pm', '6pm', '9pm', '12am', '3am', '6am', '9am'];
        this.lineChartWithNumbersAndGridOptions = this.gradientChartOptionsConfigurationWithNumbersAndGrid;

        this.lineChartWithNumbersAndGridType = 'line';

    }

    public subscribe() {
        if (this.subscribed) {
            return;
        }

        // Stream of messages
        this.messages = this._stompService.subscribe('/topic/home_out');

        // Subscribe a function to be run on_next message
        this.subscription = this.messages.subscribe(this.on_next);

        this.subscribed = true;
    }

    public unsubscribe() {
        if (!this.subscribed) {
            return;
        }

        // This will internally unsubscribe from Stomp Broker
        // There are two subscriptions - one created explicitly, the other created in the template by use of 'async'
        this.subscription.unsubscribe();
        this.subscription = null;
        this.messages = null;

        this.subscribed = false;
    }

    ngOnDestroy() {
        this.unsubscribe();
    }

    public sendMessage(message: string) {
        console.log('sending: ' + message);
        this._stompService.publish('/topic/home_in', message);
    }

    /** Consume a message from the _stompService */
    public on_next = (message: Message) => {
        const body = message.body;
        if (body === 'status:True') {
            this.watcher_status.next(true);
        } else if (body === 'status:False') {
            this.watcher_status.next(false);
        } else if (body === 'light:True') {
            this.light_status.next(true);
        } else if (body === 'light:False') {
            this.light_status.next(false);
        } else if (body === 'alarm') {
            if (this.alarm_color.value === '#ebecf1') {
                this.alarm_color.next('#ff3636');
            } else {
                this.alarm_color.next('#ebecf1');
            }
        } else if (body.includes('tmp:')) {
            const tmpValue = body.substring(4);
            const tmpTime = new Date();
            this.lineChartWithNumbersAndGridLabels.push(tmpTime.toLocaleString('en-US', {
                hour: 'numeric',
                minute: 'numeric',
                hour12: true
            }));
            if (this.lineChartWithNumbersAndGridLabels.length > 10) {
                this.lineChartWithNumbersAndGridLabels.shift();
            }
            this.tmpValues.push(tmpValue);
            if (this.tmpValues.length > 10) {
                this.tmpValues.shift();
            }
            this.tmpChart.chart.update();

        }
        // Log it to the console
        console.log(message);
    };
}
