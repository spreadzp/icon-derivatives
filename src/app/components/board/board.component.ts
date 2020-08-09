import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {
  showTable = true;
  isMobile = false;
  displayedColumns: string[] = ['addressGamer', 'numberTicket'];
  gamersTickets = [{addressGamer: 'fgj', numberTicket: 45}];
  constructor() { }

  ngOnInit() {

  }
}
