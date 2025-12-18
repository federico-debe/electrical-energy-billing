from typing import List, Optional
import pandas as pd
from pydantic import BaseModel

from common.enums import ConsumerType


class ElectricityBillSystemCosts(BaseModel):
    consumer_type: int
    consumption_kwh: List[float]  # [F1, F2, F3]
    contracted_power_kW: float
    voltage_kv: Optional[float] = None
    # ------ TARIFFE DI RETE in cent/kWh ------
    sigma_1: float = 0
    sigma_2: float = 0
    sigma_3: float = 0
    # ------ FATTORI DI PERDITA in cent/kWh ------
    per_unit_costs: float = 0
    per_kw_costs: float = 0
    per_kwh_costs: float = 0
    # ------ ONERI DI SISTEMA relativi al sostegno delle energie rinnovabili ed alla cogenerazione (ASOS) --------- 
    per_unit_costs_class_0: float = 0
    per_kw_costs_class_0: float = 0
    per_kwh_costs_class_0: float = 0
    per_unit_costs_asos_1: float = 0
    per_kw_costs_asos_1: float = 0
    per_kwh_costs_asos_1: float = 0
    per_unit_costs_asos_2: float = 0
    per_kw_costs_asos_2: float = 0
    per_kwh_costs_asos_2: float = 0
    per_unit_costs_asos_3: float = 0
    per_kw_costs_asos_3: float = 0
    per_kwh_costs_asos_3: float = 0
    per_unit_costs_val: float = 0
    per_kw_costs_val: float = 0
    per_kwh_costs_val: float = 0
    # ------ ONERI DI SISTEMA generali (ARIM, UC3, UC6) --------- 
    per_unit_costs_arim: float = 0
    per_kw_costs_arim: float = 0
    per_kwh_costs_arim: float = 0
    per_unit_costs_uc3: float = 0 
    per_kw_costs_uc3: float = 0 # €/kW/anno
    per_kwh_costs_uc3: float = 0 # €/kWh = Copertura degli squilibri di sistema per distribuzione
    per_unit_costs_uc6: float = 0 
    per_kw_costs_uc6: float = 0 # €/kW/anno = Remunerazione dei miglioramenti della continuità (fisso)
    per_kwh_costs_uc6: float = 0 # €/kWh = Remunerazione dei miglioramenti della continuità (variabile)

    @property
    def consumer_type_enum(self) -> ConsumerType:
        return ConsumerType(self.consumer_type) 
    
    def _get_total_consumption_kwh(self, consumption_kwh: list[float]) -> float:
        return sum(consumption_kwh)
    
    
    def _get_sigma_1(self) -> float:
        return self.sigma_1 * 1/12
    
    def _get_per_unit_costs(self) -> float:
        return 0 if self.per_unit_costs is None or pd.isna(self.per_unit_costs) else self.per_unit_costs / 100
    
    def _get_per_unit_costs_class_0(self) -> float:
        return 0 if self.per_unit_costs_class_0 is None or pd.isna(self.per_unit_costs_class_0) else self.per_unit_costs_class_0 / 100

    def _get_per_unit_costs_asos_1(self) -> float:
        return 0 if self.per_unit_costs_asos_1 is None or pd.isna(self.per_unit_costs_asos_1) else self.per_unit_costs_asos_1 / 100

    def _get_per_unit_costs_asos_2(self) -> float:
        return 0 if self.per_unit_costs_asos_2 is None or pd.isna(self.per_unit_costs_asos_2) else self.per_unit_costs_asos_2 / 100

    def _get_per_unit_costs_asos_3(self) -> float:
        return 0 if self.per_unit_costs_asos_3 is None or pd.isna(self.per_unit_costs_asos_3) else self.per_unit_costs_asos_3 / 100

    def _get_per_unit_costs_val(self) -> float:
        return 0 if self.per_unit_costs_val is None or pd.isna(self.per_unit_costs_val) else self.per_unit_costs_val / 100

    def _get_per_unit_costs_arim(self) -> float:
        return 0 if self.per_unit_costs_arim is None or pd.isna(self.per_unit_costs_arim) else self.per_unit_costs_arim / 100
    
    def _get_per_unit_costs_uc3(self) -> float:
        if self.per_unit_costs_uc3 is None or pd.isna(self.per_unit_costs_uc3):
            return 0
        if self.consumer_type_enum == 1: # DOMESTIC_NO_RESIDENTIAL
            return self.per_unit_costs_uc3
        else:
            return self.per_unit_costs_uc3 * 1/12
        
    def _get_per_unit_costs_uc6(self) -> float:
        if self.per_unit_costs_uc6 is None or pd.isna(self.per_unit_costs_uc6):
            return 0
        if self.consumer_type_enum == 1: # DOMESTIC_NO_RESIDENTIAL
            return self.per_unit_costs_uc6
        else:
            return self.per_unit_costs_uc6 * 1/12


    def _get_sigma_2(self, contracted_power_kW) -> float:
        return self.sigma_2 * contracted_power_kW * 1/12
    
    def _get_per_kw_costs(self, contracted_power_kW):
        if self.per_kw_costs is None or pd.isna(self.per_kw_costs):
            return 0
        return (self.per_kw_costs / 100) * contracted_power_kW 
    
    def _get_per_kw_costs_class_0(self, contracted_power_kW) -> float:
        if self.per_kw_costs_class_0 is None or pd.isna(self.per_kw_costs_class_0):
            return 0
        return (self.per_kw_costs_class_0 / 100) * contracted_power_kW
    
    def _get_per_kw_costs_asos_1(self, contracted_power_kW) -> float:
        if self.per_kw_costs_asos_1 is None or pd.isna(self.per_kw_costs_asos_1):
            return 0
        return (self.per_kw_costs_asos_1 / 100) * contracted_power_kW

    def _get_per_kw_costs_asos_2(self, contracted_power_kW) -> float:
        if self.per_kw_costs_asos_2 is None or pd.isna(self.per_kw_costs_asos_2):
            return 0
        return (self.per_kw_costs_asos_2 / 100) * contracted_power_kW

    def _get_per_kw_costs_asos_3(self, contracted_power_kW) -> float:
        if self.per_kw_costs_asos_3 is None or pd.isna(self.per_kw_costs_asos_3):
            return 0
        return (self.per_kw_costs_asos_3 / 100) * contracted_power_kW

    def _get_per_kw_costs_val(self, contracted_power_kW) -> float:
        if self.per_kw_costs_val is None or pd.isna(self.per_kw_costs_val):
            return 0
        return (self.per_kw_costs_val / 100) * contracted_power_kW
    
    def _get_per_kw_costs_arim(self, contracted_power_kW) -> float:
        if self.per_kw_costs_arim is None or pd.isna(self.per_kw_costs_arim):
            return 0
        return (self.per_kw_costs_arim / 100) * contracted_power_kW
    
    def _get_per_kw_costs_uc3(self, contracted_power_kW, ) -> float:
        if self.per_kw_costs_uc3 is None or pd.isna(self.per_kw_costs_uc3):
            return 0
        return self.per_kw_costs_uc3 * contracted_power_kW * 1/12
    
    def _get_per_kw_costs_uc6(self, contracted_power_kW) -> float:
        if self.per_kw_costs_uc6 is None or pd.isna(self.per_kw_costs_uc6):
            return 0
        return self.per_kw_costs_uc6 * contracted_power_kW * 1/12
    

    def _get_sigma_3(self, consumption_kwh: list[float]) -> float:
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return self.sigma_3 * total_kwh
    
    def _get_per_kwh_costs(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs is None or pd.isna(self.per_kwh_costs):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return (self.per_kwh_costs / 100) * total_kwh
    
    def _get_per_kwh_costs_class_0(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_class_0 is None or pd.isna(self.per_kwh_costs_class_0):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return (self.per_kwh_costs_class_0 / 100) * total_kwh

    def _get_per_kwh_costs_asos_1(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_asos_1 is None or pd.isna(self.per_kwh_costs_asos_1):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return (self.per_kwh_costs_asos_1 / 100) * total_kwh

    def _get_per_kwh_costs_asos_2(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_asos_2 is None or pd.isna(self.per_kwh_costs_asos_2):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return (self.per_kwh_costs_asos_2 / 100) * total_kwh

    def _get_per_kwh_costs_asos_3(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_asos_3 is None or pd.isna(self.per_kwh_costs_asos_3):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return (self.per_kwh_costs_asos_3 / 100) * total_kwh

    def _get_per_kwh_costs_val(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_val is None or pd.isna(self.per_kwh_costs_val):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return (self.per_kwh_costs_val / 100) * total_kwh

    def _get_per_kwh_costs_arim(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_arim is None or pd.isna(self.per_kwh_costs_arim):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return (self.per_kwh_costs_arim / 100) * total_kwh
    
    def _get_per_kwh_costs_uc3(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_uc3 is None or pd.isna(self.per_kwh_costs_uc3):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return self.per_kwh_costs_uc3 * total_kwh

    def _get_per_kwh_costs_uc6(self, consumption_kwh: list[float]) -> float:
        if self.per_kwh_costs_uc6 is None or pd.isna(self.per_kwh_costs_uc6):
            return 0
        total_kwh = self._get_total_consumption_kwh(consumption_kwh)
        return self.per_kwh_costs_uc6 * total_kwh
    

    def calculate_electricity_bill_system_costs( 
            self,
            consumer_type: int,
            consumption_kwh,
            contracted_power_kW: float, 
            voltage_kv: Optional[float] = None
        ):
            per_unit_costs = 0
            per_kw_costs = 0
            per_kwh_costs = 0
            
            if consumer_type == 0 or consumer_type == 1: # DOMESTIC
                # ------ TARIFFE DI RETE ------
                per_unit_costs += self._get_sigma_1()
                per_kw_costs += self._get_sigma_2(contracted_power_kW)
                per_kwh_costs += self._get_sigma_3(consumption_kwh)
            elif consumer_type not in [2, 3, 5]: # PUBLIC_LIGHTING (BT/MT) and PUBLIC_CHARGING_INFRASTRUCTURES_FOR_ELECTRIC_VEHICLES
                apply_loss_factors = True
                if consumer_type == 4:
                    if contracted_power_kW > 16.5: 
                        # consumatore speciale o industriale, alcune tariffe di rete potrebbero non applicarsi o essere pagate indirettamente
                        apply_loss_factors = False
                if apply_loss_factors:
                    # ------ FATTORI DI PERDITA ------
                    per_unit_costs += self._get_per_unit_costs()
                    per_kw_costs += self._get_per_kw_costs(contracted_power_kW)
                    per_kwh_costs += self._get_per_kwh_costs(consumption_kwh)

            # ------ ONERI DI SISTEMA ---------
            for oneri_prefix in ["arim", "uc3", "uc6"]:
                per_unit_costs += getattr(self, f"_get_per_unit_costs_{oneri_prefix}")()
                per_kw_costs += getattr(self, f"_get_per_kw_costs_{oneri_prefix}")(contracted_power_kW)
                per_kwh_costs += getattr(self, f"_get_per_kwh_costs_{oneri_prefix}")(consumption_kwh)

            if consumer_type == 0 and contracted_power_kW <= 3: # BT domestico residente
                per_unit_costs += self._get_per_unit_costs_class_0()
                per_kw_costs += self._get_per_kw_costs_class_0(contracted_power_kW)
                per_kwh_costs += self._get_per_kwh_costs_class_0(consumption_kwh)
            elif consumer_type == 1 and contracted_power_kW <= 3: # BT domestico non residente
                per_unit_costs += self._get_per_unit_costs_asos_1()
                per_kw_costs += self._get_per_kw_costs_asos_1(contracted_power_kW)
                per_kwh_costs += self._get_per_kwh_costs_asos_1(consumption_kwh)
            elif (
                (consumer_type in [2, 3, 4, 5]) or # BT non domestiche, illuminazione pubblica, ricarica EV
                (consumer_type == 0 and contracted_power_kW > 3) or  # BT domestico residente > 3 kW
                (consumer_type == 1 and contracted_power_kW > 3) or  # BT domestico non residente > 3 kW
                (consumer_type == 6 and contracted_power_kW <= 100) 
            ):
                per_unit_costs += self._get_per_unit_costs_asos_2()
                per_kw_costs += self._get_per_kw_costs_asos_2(contracted_power_kW)
                per_kwh_costs += self._get_per_kwh_costs_asos_2(consumption_kwh)
                
            elif (
                (consumer_type == 6 and contracted_power_kW > 100) or # Media tensione
                consumer_type == 7 or # Alta tensione
                (consumer_type == 8 and voltage_kv is not None and voltage_kv < 380)
            ): 
                per_unit_costs += self._get_per_unit_costs_asos_3()
                per_kw_costs += self._get_per_kw_costs_asos_3(contracted_power_kW)
                per_kwh_costs += self._get_per_kwh_costs_asos_3(consumption_kwh)
            elif consumer_type == 8 and voltage_kv is not None and voltage_kv >= 380: # Altissima tensione >=380 kV
                per_unit_costs += self._get_per_unit_costs_val()
                per_kw_costs += self._get_per_kw_costs_val(contracted_power_kW)
                per_kwh_costs += self._get_per_kwh_costs_val(consumption_kwh)

            return per_unit_costs, per_kw_costs, per_kwh_costs
    
