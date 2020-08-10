import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {
  showTable = true;
  isMobile = false;
  displayedColumns: string[] = ['nameDerivative', 'expirationPrice', 'currentPrice', 'blockExpiration', 'timeExpiration', 'deposit', 'buy', 'sell'];
  gamersTickets = [
    {
      nameDerivative: 'fgj', expirationPrice: 55,
      currentPrice: 45, blockExpiration: 123456, timeExpiration: new Date(), deposit: 50
    },
    {
      nameDerivative: 'fgj', expirationPrice: 65,
      currentPrice: 45, blockExpiration: 123886, timeExpiration: new Date(), deposit: 56
    }
  ];
  constructor() { }

  ngOnInit() {

  }

  buyDerivative(ticket) {
    console.log('buy ticket :>> ', ticket);
  }

  sellDerivative(ticket) {
    console.log('sell ticket :>> ', ticket);
  }
}
