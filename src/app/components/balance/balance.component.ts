import { Component, OnInit } from '@angular/core';
import { IconProviderService } from 'src/app/services/icon-provider.service';

@Component({
  selector: 'app-balance',
  templateUrl: './balance.component.html',
  styleUrls: ['./balance.component.scss']
})
export class BalanceComponent implements OnInit {
  result = null;
  constructor(private iconProviderService: IconProviderService) { }

  ngOnInit(): void {
    this.result = this.iconProviderService.getWallet()
    .then(res => this.result = res);
  }

}
