import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatTableModule} from '@angular/material/table';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatIconModule} from '@angular/material/icon';
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';
// import {
//   MatButtonModule,
//   MatCardModule,
//   MatFormFieldModule,
//   MatInputModule,
//   MatToolbarModule,
//   MatSidenavModule,
//   MatListModule,
//   MatIconModule,
//   MatSnackBarModule
// } from '@angular/material';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { FooterComponent } from './components/footer/footer.component';
import { HeaderComponent } from './components/header/header.component';
import { BalanceComponent } from './components/balance/balance.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { IconProviderService } from './services/icon-provider.service';
import { PriceService } from './services/price.service';
import { PriceComponent } from './components/price/price.component';
import { HttpClientModule } from '@angular/common/http';
import { BoardComponent } from './components/board/board.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { InfoComponent } from './components/info/info.component';
import { RulesComponent } from './components/rules/rules.component';
import { StatisticComponent } from './components/statistic/statistic.component';
import { ExchangeComponent } from './components/exchange/exchange.component';
import { ShowPageService } from './services/show-page.service';
import { CabinetComponent } from './components/cabinet/cabinet.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    FooterComponent,
    HeaderComponent,
    BalanceComponent,
    NotFoundComponent,
    PriceComponent,
    BoardComponent,
    InfoComponent,
    RulesComponent,
    StatisticComponent,
    ExchangeComponent,
    CabinetComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule,
    MatTableModule,
    MatSidenavModule,
    MatCardModule,
    MatButtonModule,
    MatIconModule,
    MatSnackBarModule
  ],
  providers: [IconProviderService, PriceService, ShowPageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
